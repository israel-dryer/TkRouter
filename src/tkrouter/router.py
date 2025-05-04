import re
from .utils import strip_query, extract_query_params, normalize_route_config
from .history import History
from .exceptions import (
    RouteNotFoundError,
    NavigationGuardError,
    RouterError  # For catch-all internal use if needed
)

# --- Singleton instance ---
_router_instance = None


def create_router(routes, outlet, transition_handler=None):
    """
    Creates the singleton Router instance. Can only be created once.

    Args:
        routes (dict): The routing configuration.
        outlet (RouterOutlet): The outlet where views are rendered.
        transition_handler (Callable): Optional global transition function.

    Returns:
        Router: The singleton router instance.

    Raises:
        RuntimeError: If the router is created more than once.
    """
    global _router_instance
    if _router_instance is not None:
        raise RuntimeError("Router has already been created.")
    _router_instance = Router(routes, outlet, transition_handler)
    return _router_instance


def get_router():
    """
    Retrieves the singleton Router instance.

    Returns:
        Router: The existing router instance.

    Raises:
        RuntimeError: If the router has not been created yet.
    """
    if _router_instance is None:
        raise RuntimeError("Router has not been created.")
    return _router_instance


class Router:
    """
    Router controls view rendering, navigation, and transition logic.

    Attributes:
        routes (dict): The routing configuration.
        outlet (RouterOutlet): The widget responsible for rendering views.
        transition_handler (Callable): Default transition function.
        history (History): Stack-based navigation history.
        _listeners (list): List of route change listeners.
    """

    def __init__(self, routes, outlet, transition_handler=None):
        self.routes = routes
        self.outlet = outlet
        self.transition_handler = transition_handler
        self.history = History()
        self._listeners = []

    def navigate(self, path, transition=None):
        """
        Navigates to a new path, resolving the route and rendering the view.

        Args:
            path (str): Path to navigate to (can include query parameters).
            transition (Callable): Optional transition override.

        Raises:
            RouteNotFoundError: If no route matches the path.
            NavigationGuardError: If a route's guard blocks access.
        """
        query_params = extract_query_params(path)
        path = strip_query(path)

        match, params, view_class, route_config = self._resolve_route(path)
        if view_class is None:
            raise RouteNotFoundError(f"Route not found for path: {path}")

        # Run navigation guard if applicable
        if isinstance(route_config, dict):
            guard = route_config.get("guard")
            redirect_path = route_config.get("redirect")
            if guard and not guard():
                if redirect_path:
                    return self.navigate(redirect_path)
                raise NavigationGuardError(f"Access denied to path: {path}")

        handler = transition or route_config.get("transition") or self.transition_handler
        params.update(query_params)

        try:
            if handler:
                handler(self.outlet, view_class, params)
            else:
                self.set_view(view_class, params)

            query_string = "&".join(f"{k}={v}" for k, v in query_params.items())
            full_path = path + ("?" + query_string if query_string else "")
            self.history.push(full_path)
            self._notify_listeners(path, params)

        except Exception as e:
            print(f"[TkRouter] Error navigating to '{path}': {e}")

    def back(self):
        """Navigate to the previous route in history."""
        try:
            path = self.history.back()
            if path:
                self.navigate(path)
        except Exception as e:
            print(f"[TkRouter] Back navigation failed: {e}")

    def forward(self):
        """Navigate to the next route in history."""
        try:
            path = self.history.forward()
            if path:
                self.navigate(path)
        except Exception as e:
            print(f"[TkRouter] Forward navigation failed: {e}")

    def go(self, delta):
        """Navigate to a relative path in the history stack."""
        try:
            path = self.history.go(delta)
            if path:
                self.navigate(path)
        except Exception as e:
            print(f"[TkRouter] Go({delta}) navigation failed: {e}")

    def set_view(self, view_class, params=None):
        """
        Directly sets a view in the outlet.

        Args:
            view_class (type): A subclass of `tk.Frame` to instantiate.
            params (dict): Optional navigation parameters.
        """
        self.outlet.set_view(view_class, params)
        if hasattr(self.outlet.current_view, "router"):
            self.outlet.current_view.router = self

    def _resolve_route(self, path):
        """
        Finds the route matching the given path.

        Args:
            path (str): The path to match (no query string).

        Returns:
            Tuple[str, dict, class, dict]: (pattern, params, view_class, route_config)
        """

        def search(route_tree, base=""):
            fallback = None
            for pattern, config in route_tree.items():
                if pattern == "*":
                    fallback = config
                    continue

                full_path = base + pattern
                param_names = re.findall(r"<([^>]+)>", full_path)
                regex_pattern = re.sub(r"<[^>]+>", r"([^/]+)", full_path)
                match = re.fullmatch(regex_pattern, path)
                if match:
                    params = dict(zip(param_names, match.groups()))
                    if isinstance(config, dict):
                        view_class = config.get("view")
                        return pattern, params, view_class, config
                    else:
                        return pattern, params, config, normalize_route_config(config)

                if isinstance(config, dict) and "children" in config:
                    result = search(config["children"], base + pattern)
                    if result[2]:  # view_class is not None
                        return result

            if fallback:
                return "*", {}, fallback, normalize_route_config(fallback)
            return None, {}, None, None

        return search(self.routes)

    def on_change(self, callback):
        """
        Subscribes a callback to be triggered on every successful route change.

        Args:
            callback (Callable): Function called with (path, params).
        """
        self._listeners.append(callback)

    def _notify_listeners(self, path, params):
        """
        Notifies all registered listeners of a route change.

        Args:
            path (str): The path navigated to.
            params (dict): The resolved route parameters.
        """
        for callback in self._listeners:
            try:
                callback(path, params)
            except Exception as e:
                print(f"[TkRouter] Route observer error: {e}")
