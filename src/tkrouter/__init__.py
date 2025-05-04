"""
tkrouter: A minimal routing system for Tkinter GUI applications.

This package provides declarative routing for Tkinter apps, including:

- Route pattern matching with path parameters (`<id>`)
- Query parameter support (`/users?tab=info`)
- Optional route guards and redirects
- Animated view transitions
- Routed widgets (`RouteLinkButton`, `RouteLinkLabel`)
- History management (back/forward/go)
- Routed base views (`RoutedView`, `StyledRoutedView`)

Example:

```python
from tkinter import Tk
from tkrouter import (
    create_router, RouterOutlet, RoutedView,
    RouteLinkButton, slide_transition
)

class Home(RoutedView):
    def __init__(self, master):
        super().__init__(master)
        RouteLinkButton(self, "/about", text="Go to About").pack()

class About(RoutedView):
    def __init__(self, master):
        super().__init__(master)
        RouteLinkButton(self, "/", text="Back to Home").pack()

ROUTES = {
    "/": Home,
    "/about": {
        "view": About,
        "transition": slide_transition
    }
}

root = Tk()
outlet = RouterOutlet(root)
outlet.pack(fill="both", expand=True)
create_router(ROUTES, outlet).navigate("/")
root.mainloop()
"""

from .router import Router, create_router, get_router
from .exceptions import RouteNotFoundError, NavigationGuardError
from .router_outlet import RouterOutlet
from .views import RoutedView, StyledRoutedView
from .widgets import RouteLinkButton, RouteLinkLabel, bind_route, with_route
from .transitions import slide_transition, simple_fade_transition

__all__ = [
    "Router",
    "create_router",
    "get_router",
    "RouteNotFoundError",
    "NavigationGuardError",
    "RouterOutlet",
    "RoutedView",
    "StyledRoutedView",
    "RouteLinkButton",
    "RouteLinkLabel",
    "bind_route",
    "with_route",
    "slide_transition",
    "simple_fade_transition",
]
