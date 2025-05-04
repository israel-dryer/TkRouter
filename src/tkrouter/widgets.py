import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict
from .utils import format_path
from .types import CommandWidget
from . import get_router


class RouteLinkButton(ttk.Button):
    def __init__(self, master: tk.Widget, to: str, params: Optional[dict] = None, **kwargs):
        self.to = to
        self.params = params
        super().__init__(master, command=self.navigate, **kwargs)

    def navigate(self):
        path = format_path(self.to, self.params)
        get_router().navigate(path)


class RouteLinkLabel(ttk.Label):
    """
    A label that acts as a clickable navigation link.
    """

    def __init__(self, master: tk.Widget, to: str, params: Optional[Dict] = None, **kwargs):
        self.to = to
        self.params = params
        super().__init__(master, **kwargs)

        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", lambda e: self.configure(font=(self._get_font(), "underline")))
        self.bind("<Leave>", lambda e: self.configure(font=(self._get_font(), "normal")))

        self.configure(cursor="hand2", foreground="blue")

    def _get_font(self):
        try:
            return self.cget("font")
        except Exception:
            return "TkDefaultFont"

    def _on_click(self, event=None):
        path = format_path(self.to, self.params)
        get_router().navigate(path)


def bind_route(widget: CommandWidget, path: str, params: Optional[dict] = None) -> None:
    formatted = format_path(path, params)
    widget.configure(command=lambda: get_router().navigate(formatted))


def with_route(path: str, params: Optional[dict] = None) -> Callable:
    formatted = format_path(path, params)

    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._router_path = formatted
        wrapper._router = get_router()
        return wrapper

    return decorator
