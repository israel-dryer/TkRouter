class RouterError(Exception):
    """Base exception for all routing-related errors."""
    pass


class RouteNotFoundError(RouterError):
    """Raised when no route matches the requested path."""
    def __init__(self, message="No route matched the requested path."):
        super().__init__(message)


class NavigationGuardError(RouterError):
    """Raised when navigation is blocked by a route guard."""
    def __init__(self, message="Navigation blocked by route guard."):
        super().__init__(message)


class InvalidRouteConfigError(RouterError):
    """Raised when a route configuration is invalid or incomplete."""
    def __init__(self, message="Invalid or incomplete route configuration."):
        super().__init__(message)

class HistoryNavigationError(RouterError):
    """Raised when navigating beyond the bounds of the history stack."""
    def __init__(self, message="History navigation out of bounds."):
        super().__init__(message)
