import tkinter as tk

from src.tkrouter.route_view import RouteView

class DummyView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.entered = False
        self.left = False

    def on_enter(self, params):
        self.entered = True

    def on_leave(self):
        self.left = True


def test_set_view_calls_lifecycle():
    root = tk.Tk()
    view = RouteView(root)
    v1 = DummyView(view)
    v2 = DummyView(view)
    view.current_view = v1
    v1.on_leave = lambda: setattr(v1, 'left', True)
    v2.on_enter = lambda p: setattr(v2, 'entered', True)
    v1.destroy = lambda: None  # prevent actual destruction for test

    def dummy_class(master):
        return v2

    view.set_view(dummy_class, {})
    assert v2.entered is True
    assert v1.left is True


def test_initial_set_view():
    root = tk.Tk()
    view = RouteView(root)
    v1 = DummyView(view)

    def dummy_class(master):
        return v1

    view.set_view(dummy_class, {})
    assert v1.entered is True
