import re
from urllib.parse import parse_qs
from .history import History


class Router:
    def __init__(self, routes, outlet, transition_handler=None):
        self.routes = routes
        self.outlet = outlet
        self.transition_handler = transition_handler
        self.history = History()

    def navigate(self, path, transition=None):
        url, _, query = path.partition("?")
        path = url
        query_params = {k: v[0] for k, v in parse_qs(query).items()} if query else {}

        match, params, view_class, route_config = self._resolve_route(path)
        if view_class is None:
            raise ValueError(f"Route not found for path: {path}")

        if isinstance(route_config, dict):
            guard = route_config.get("guard")
            redirect_path = route_config.get("redirect")
            if guard and not guard():
                if redirect_path:
                    return self.navigate(redirect_path)
                return

        handler = transition or route_config.get("transition") or self.transition_handler
        params.update(query_params)

        try:
            if handler:
                handler(self.outlet, view_class, params)
            else:
                self.outlet.set_view(view_class, params)
            self.history.push(path + ("?" + query if query else ""))
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
                        return pattern, params, config, {"view": config}

                if isinstance(config, dict) and "children" in config:
                    result = search(config["children"], base + pattern)
                    if result[2]:
                        return result

            if fallback:
                return "*", {}, fallback, {"view": fallback} if not isinstance(fallback, dict) else fallback
            return None, {}, None, None

        return search(self.routes)
