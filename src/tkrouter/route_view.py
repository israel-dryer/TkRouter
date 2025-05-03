import tkinter as tk

class RouteView(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.current_view = None

    def set_view(self, view_class, params):
        if self.current_view:
            if hasattr(self.current_view, 'on_leave'):
                self.current_view.on_leave()
            self.current_view.destroy()

        self.current_view = view_class(self)

        if hasattr(self.current_view, 'on_enter'):
            self.current_view.on_enter(params)

        self.current_view.pack(fill="both", expand=True)
