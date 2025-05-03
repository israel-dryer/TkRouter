class RouteNotFoundError(Exception):
    """Raised when no route matches the requested path."""
    pass

class NavigationGuardError(Exception):
    """Raised when navigation is blocked by a route guard."""
    pass

class InvalidRouteConfigError(Exception):
    """Raised when a route configuration is invalid or incomplete."""
    pass
