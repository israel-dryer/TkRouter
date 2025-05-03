import tkinter as tk

class ChildRouteView(tk.Frame):
    def __init__(self, master, router, base_path):
        super().__init__(master)
        self.router = router
        self.base_path = base_path.rstrip("/")
        self.current_view = None
        self.pack(fill="both", expand=True)
        self.check_for_child_route()

    def check_for_child_route(self):
        current_path = self.router.history.current() or ""
        if current_path.startswith(self.base_path + "/"):
            _, params, view_class, _ = self.router._resolve_route(current_path)
            if view_class:
                self.set_view(view_class, params)
        self.after(250, self.check_for_child_route)

    def set_view(self, view_class, params):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self)
        self.current_view.pack(fill="both", expand=True)
        if hasattr(self.current_view, "on_navigate"):
            self.current_view.on_navigate(params)
