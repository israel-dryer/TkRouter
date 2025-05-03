import tkinter as tk

class RouteView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.current_view = None
        self.router = None
        self.pack(fill="both", expand=True)

    def set_view(self, view_class, params=None):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self)
        self.current_view.pack(fill="both", expand=True)
        if hasattr(self.current_view, "on_navigate"):
            self.current_view.on_navigate(params or {})
