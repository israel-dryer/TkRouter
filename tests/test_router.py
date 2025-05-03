import pytest
from src.tkrouter.router import Router

class DummyView:
    def __init__(self, master):
        self.master = master

class DummyOutlet:
    def __init__(self):
        self.view = None
        self.view_path = None

    def set_view(self, view_class, params):
        self.view = view_class(self)
        self.view_path = params.get("__path__", "")


def test_basic_navigation():
    outlet = DummyOutlet()
    router = Router(routes={"/": DummyView}, outlet=outlet)
    router.navigate("/")
    assert isinstance(outlet.view, DummyView)


def test_guard_and_redirect():
    outlet = DummyOutlet()
    routes = {
        "/secure": {
            "view": DummyView,
            "guard": lambda: False,
            "redirect": "/login"
        },
        "/login": DummyView
    }
    router = Router(routes=routes, outlet=outlet)
    router.navigate("/secure")
    assert isinstance(outlet.view, DummyView)


def test_404_fallback():
    outlet = DummyOutlet()
    router = Router(routes={"*": DummyView}, outlet=outlet)
    router.navigate("/unknown")
    assert isinstance(outlet.view, DummyView)


def test_history_stack():
    outlet = DummyOutlet()
    router = Router(routes={"/": DummyView, "/next": DummyView}, outlet=outlet)
    router.navigate("/")
    router.navigate("/next")
    router.back()
    assert isinstance(outlet.view, DummyView)
