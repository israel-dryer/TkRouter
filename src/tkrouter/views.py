import tkinter as tk
from tkinter import ttk
from typing import Optional, Dict, Any
from tkrouter import get_router


class RoutedView(tk.Frame):
    """
    Base class for views rendered by the router using tk.Frame.

    Automatically sets `self.router` and `self.params`, and provides
    an overridable `on_navigate()` method for handling route params.
    """

    def __init__(self, master: Optional[tk.Misc] = None, **kwargs):
        """
        Args:
            master (tk.Misc): Parent widget.
            kwargs: Accepts 'params' from the router.
        """
        super().__init__(master)
        self.router = get_router()
        self.params: Dict[str, Any] = kwargs.get("params", {})

    def on_navigate(self, params: Dict[str, Any]) -> None:
        """
        Called by the router when this view is navigated to.

        Override this in subclasses to respond to parameters (e.g., query strings or path params).
        """
        pass


class StyledRoutedView(ttk.Frame):
    """
    Base class for ttk.Frame-based views rendered by the router.

    Like RoutedView, but uses themed ttk styling. Subclass this when building
    views with ttk widgets.
    """

    def __init__(self, master: Optional[tk.Misc] = None, **kwargs):
        """
        Args:
            master (tk.Misc): Parent widget.
            kwargs: Accepts 'params' from the router.
        """
        super().__init__(master)
        self.router = get_router()
        self.params: Dict[str, Any] = kwargs.get("params", {})

    def on_navigate(self, params: Dict[str, Any]) -> None:
        """
        Called by the router when this view is navigated to.

        Override this in subclasses to react to navigation parameters.
        """
        pass
