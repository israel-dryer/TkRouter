import pytest
import tkinter as tk

from tkrouter.exceptions import RouteNotFoundError

try:
    root_test = tk.Tk()
    root_test.destroy()
except tk.TclError:
    pytest.skip("Tkinter not supported in this environment", allow_module_level=True)


import pytest
from unittest.mock import Mock
from tkrouter.router import Router
from tkrouter.router_outlet import RouterOutlet
import tkinter as tk

class DummyPage(tk.Frame):
    def on_navigate(self, params):
        self.params = params

def test_navigate_sets_view_and_history():
    root = tk.Tk()
    outlet = RouterOutlet(root)
    routes = {"/": DummyPage}
    router = Router(routes=routes, outlet=outlet)
    router.navigate("/")
    assert isinstance(outlet.winfo_children()[0], DummyPage)
    assert router.history.current() == "/"
    root.destroy()

def test_guard_redirect():
    root = tk.Tk()
    outlet = RouterOutlet(root)
    routes = {
        "/secure": {"view": DummyPage, "guard": lambda: False, "redirect": "/"},
        "/": DummyPage
    }
    router = Router(routes=routes, outlet=outlet)
    router.navigate("/secure")
    assert router.history.current() == "/"
    root.destroy()

def test_route_not_found():
    root = tk.Tk()
    outlet = RouterOutlet(root)
    routes = {"/": DummyPage}
    router = Router(routes=routes, outlet=outlet)
    with pytest.raises(RouteNotFoundError):
        router.navigate("/missing")
    root.destroy()