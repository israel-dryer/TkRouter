import tkinter as tk
from typing import Optional, Type


class RouterOutlet(tk.Frame):
    """
    A dynamic container for routing views.

    The RouterOutlet acts as the placeholder for views rendered by the Router.
    It dynamically replaces its contents with the appropriate view class whenever
    navigation occurs.

    Attributes:
        current_view (tk.Widget): The currently displayed view, or None if unset.
        router (Any): A reference to the router that controls this outlet.
    """

    def __init__(self, master: tk.Misc):
        """
        Initializes the outlet with no current view.

        Args:
            master (tk.Misc): The parent widget (typically a root or container frame).
        """
        super().__init__(master)
        self.current_view: Optional[tk.Widget] = None
        self.router = None
        self.pack(fill="both", expand=True)

    def set_view(self, view_class: Type[tk.Widget], params: Optional[dict] = None):
        """
        Renders the specified view in the outlet, replacing any existing view.

        If the view defines an `on_navigate(params)` method, it will be invoked
        after rendering.

        Args:
            view_class (type): A subclass of tk.Widget to instantiate.
            params (dict, optional): Optional parameters passed to the new view.
        """
        if self.current_view and self.current_view.winfo_exists():
            self.current_view.destroy()

        self.current_view = view_class(self)
        self.current_view.pack(fill="both", expand=True)

        if hasattr(self.current_view, "on_navigate"):
            self.current_view.on_navigate(params or {})
