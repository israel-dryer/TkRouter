import pytest
import tkinter as tk
from tkrouter.router import Router
from tkrouter.route_view import RouteView
from tkrouter.exceptions import RouteNotFoundError, NavigationGuardError

class DummyPage(tk.Frame):
    pass

def test_route_not_found_exception():
    root = tk.Tk()
    outlet = RouteView(root)
    router = Router(routes={"/": DummyPage}, outlet=outlet)

    with pytest.raises(RouteNotFoundError):
        router.navigate("/invalid")
    root.destroy()

def test_navigation_guard_exception():
    root = tk.Tk()
    outlet = RouteView(root)
    routes = {
        "/secure": {
            "view": DummyPage,
            "guard": lambda: False
        }
    }
    router = Router(routes=routes, outlet=outlet)

    with pytest.raises(NavigationGuardError):
        router.navigate("/secure")
    root.destroy()
