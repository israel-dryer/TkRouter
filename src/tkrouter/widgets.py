import tkinter as tk

def format_path(path, params):
    if not params:
        return path

    path_filled = path
    query_items = {}
    for key, val in params.items():
        if f"<{key}>" in path:
            path_filled = path_filled.replace(f"<{key}>", str(val))
        else:
            query_items[key] = val

    if query_items:
        path_filled += "?" + "&".join(f"{k}={v}" for k, v in query_items.items())

    return path_filled


class RouteLinkButton(tk.Button):
    def __init__(self, master, router, to, params=None, **kwargs):
        super().__init__(master, **kwargs)
        self.router = router
        self.to = to
        self.params = params
        self.configure(command=self.navigate)

    def navigate(self):
        path = format_path(self.to, self.params)
        self.router.navigate(path)

def bind_route(widget, router, path, params=None):
    path = format_path(path, params)
    widget.configure(command=lambda: router.navigate(path))

def with_route(router, path, params=None):
    path = format_path(path, params)
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._router_path = path
        wrapper._router = router
        return wrapper
    return decorator
