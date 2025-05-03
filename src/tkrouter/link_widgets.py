import tkinter as tk

class RouteLinkButton(tk.Button):
    def __init__(self, master, router, to, **kwargs):
        super().__init__(master, **kwargs)
        self.router = router
        self.to = to
        self.configure(command=self.navigate)

    def navigate(self):
        self.router.navigate(self.to)


def bind_route(widget, router, path):
    widget.configure(command=lambda: router.navigate(path))


def with_route(router, path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._router_path = path
        wrapper._router = router
        return wrapper
    return decorator
