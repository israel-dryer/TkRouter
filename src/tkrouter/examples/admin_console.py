import tkinter as tk
from tkinter import ttk
from tkrouter import create_router, get_router
from tkrouter.router_outlet import RouterOutlet
from tkrouter.transitions import slide_transition
from tkrouter.widgets import RouteLinkButton
from tkrouter.views import StyledRoutedView


class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2d2d30", width=140)
        self.pack_propagate(False)
        ttk.Label(self, text="Admin", background="#2d2d30", foreground="white", font=("Segoe UI", 14)).pack(pady=(20, 10))

        RouteLinkButton(self, "/", text="Dashboard").pack(fill="x", padx=10, pady=2)
        RouteLinkButton(self, "/users", text="Users").pack(fill="x", padx=10, pady=2)
        RouteLinkButton(self, "/reports", text="Reports").pack(fill="x", padx=10, pady=2)

        ttk.Label(self, text="Logs", background="#2d2d30", foreground="#ccc").pack(pady=(15, 0))
        RouteLinkButton(self, "/logs", params={"level": "info"}, text="Info Logs").pack(fill="x", padx=10, pady=1)
        RouteLinkButton(self, "/logs", params={"level": "error"}, text="Error Logs").pack(fill="x", padx=10, pady=1)


class DashboardPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="Dashboard", font=("Segoe UI", 18)).pack(pady=(20, 10))
        ttk.Label(self, text="Welcome to the admin dashboard.", font=("Segoe UI", 12)).pack()


class UsersPage(StyledRoutedView):
    def __init__(self, master=None):
        super().__init__(master)
        ttk.Label(self, text="Users", font=("Segoe UI", 18)).pack(pady=(20, 10))
        for user_id in range(1, 4):
            RouteLinkButton(self, "/users/<id>", params={"id": user_id}, text=f"User {user_id}").pack(pady=2)


class UserDetailsPage(StyledRoutedView):
    def __init__(self, master=None):
        super().__init__(master)
        self.label = ttk.Label(self, font=("Segoe UI", 14))
        self.label.pack(pady=20)

    def on_navigate(self, params: dict):
        self.label.config(text=f"User Details for ID: {params.get('id')}")


class ReportsPage(StyledRoutedView):
    def __init__(self, master=None):
        super().__init__(master)
        ttk.Label(self, text="Reports", font=("Segoe UI", 18)).pack(pady=20)


class LogsPage(StyledRoutedView):
    def __init__(self, master=None):
        super().__init__(master)
        ttk.Label(self, text="Logs", font=("Segoe UI", 18)).pack(pady=(20, 10))
        self.label = ttk.Label(self, font=("Segoe UI", 14))
        self.label.pack(pady=10)

    def on_navigate(self, params: dict):
        level = params.get("level", "all")
        self.label.config(text=f"Showing logs with level: {level}")


ROUTES = {
    "/": DashboardPage,
    "/users": UsersPage,
    "/users/<id>": UserDetailsPage,
    "/reports": {
        "view": ReportsPage,
        "transition": slide_transition
    },
    "/logs": LogsPage,
    "*": lambda master=None: ttk.Label(master, text="404 - Page Not Found", font=("Segoe UI", 16))
}


def run():
    root = tk.Tk()
    root.title("Admin Console Example")
    root.geometry("600x400")

    style = ttk.Style()
    style.theme_use("clam")

    container = ttk.Frame(root)
    container.pack(fill="both", expand=True)

    outlet = RouterOutlet(container)
    outlet.pack(side="right", fill="both", expand=True)

    sidebar = Sidebar(container)
    sidebar.pack(side="left", fill="y")

    create_router(ROUTES, outlet)
    get_router().navigate("/")

    root.mainloop()


if __name__ == "__main__":
    run()
