import tkinter as tk
from tkinter import ttk
from tkrouter import create_router, get_router
from tkrouter.router_outlet import RouterOutlet
from tkrouter.views import StyledRoutedView
from tkrouter.widgets import RouteLinkButton


class HomePage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🏠 Home", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="Welcome to the home page.").pack(pady=5)
        RouteLinkButton(self, "/about", text="Go to About").pack(pady=10)


class AboutPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="ℹ️ About", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="This is the about page.").pack(pady=5)
        RouteLinkButton(self, "/", text="Back to Home").pack(pady=10)


ROUTES = {
    "/": HomePage,
    "/about": AboutPage,
}


def run():
    root = tk.Tk()
    root.title("TkRouter Example")
    root.geometry("400x250")

    style = ttk.Style()
    style.theme_use("clam")

    outlet = RouterOutlet(root)
    outlet.pack(fill="both", expand=True)

    create_router(ROUTES, outlet)
    get_router().navigate("/")

    root.mainloop()


if __name__ == "__main__":
    run()
