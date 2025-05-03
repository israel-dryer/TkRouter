import re
from .utils import strip_query, extract_query_params, normalize_route_config
from .history import History
from .exceptions import RouteNotFoundError, NavigationGuardError


class Router:
    def __init__(self, routes, outlet, transition_handler=None):
        self.routes = routes
        self.outlet = outlet
        self.transition_handler = transition_handler
        self.history = History()
        self._listeners = []

    def navigate(self, path, transition=None):
        query_params = extract_query_params(path)
        path = strip_query(path)

        match, params, view_class, route_config = self._resolve_route(path)
        if view_class is None:
            raise RouteNotFoundError(f"Route not found for path: {path}")

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
                self.outlet.set_view(view_class, params)
            query_string = "&".join(f"{k}={v}" for k, v in query_params.items())
            full_path = path + ("?" + query_string if query_string else "")
            self.history.push(full_path)
            self._notify_listeners(path, params)
        except Exception as e:
            print(f"[TkRouter] Error navigating to '{path}': {e}")

    def back(self):
        path = self.history.back()
        if path:
            self.navigate(path)

    def forward(self):
        path = self.history.forward()
        if path:
            self.navigate(path)

    def go(self, delta):
        path = self.history.go(delta)
        if path:
            self.navigate(path)

    def _resolve_route(self, path):
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
                    if result[2]:
                        return result

            if fallback:
                return "*", {}, fallback, normalize_route_config(fallback)
            return None, {}, None, None

        return search(self.routes)

    def on_change(self, callback):
        """Register a listener for route changes."""
        self._listeners.append(callback)

    def _notify_listeners(self, path, params):
        for callback in self._listeners:
            try:
                callback(path, params)
            except Exception as e:
                print(f"[TkRouter] Route observer error: {e}")
