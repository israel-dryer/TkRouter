import tkinter as tk
from tkinter import ttk
from tkrouter import create_router, get_router
from tkrouter.router_outlet import RouterOutlet
from tkrouter.widgets import RouteLinkButton
from tkrouter.transitions import slide_transition
from tkrouter.views import StyledRoutedView


class HomePage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🏠 Home", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="Welcome to the unified router demo!").pack()
        RouteLinkButton(self, "/dashboard", text="Go to Dashboard").pack(pady=10)


class DashboardPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="📊 Dashboard", font=("Segoe UI", 18)).pack(pady=10)
        RouteLinkButton(self, "/dashboard/stats", text="Stats").pack(pady=5)
        RouteLinkButton(self, "/dashboard/settings", text="Settings").pack(pady=5)
        RouteLinkButton(self, "/", text="← Back to Home").pack(pady=20)


class StatsPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="📈 Stats View", font=("Segoe UI", 16)).pack(pady=10)
        ttk.Label(self, text="Some stats go here...").pack()
        RouteLinkButton(self, "/dashboard", text="← Back to Dashboard").pack(pady=10)


class SettingsPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="⚙️ Settings View", font=("Segoe UI", 16)).pack(pady=10)
        ttk.Label(self, text="Settings options appear here.").pack()
        RouteLinkButton(self, "/dashboard", text="← Back to Dashboard").pack(pady=10)


ROUTES = {
    "/": HomePage,
    "/dashboard": DashboardPage,
    "/dashboard/stats": {"view": StatsPage, "transition": slide_transition},
    "/dashboard/settings": SettingsPage,
}

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TkRouter – Unified Routing Example")
    root.geometry("500x350")

    ttk.Style().theme_use("clam")

    outlet = RouterOutlet(root)
    outlet.pack(fill="both", expand=True)

    create_router(ROUTES, outlet)
    get_router().navigate("/")

    root.mainloop()
