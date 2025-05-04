import tkinter as tk
from tkinter import ttk
from tkrouter import create_router, get_router
from tkrouter.router_outlet import RouterOutlet
from tkrouter.widgets import RouteLinkButton
from tkrouter.views import StyledRoutedView
from tkrouter.exceptions import NavigationGuardError

# --- Guard condition ---
logged_in = False


def is_authenticated():
    return logged_in


# --- Views ---

class HomePage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🏠 Home", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="Try accessing the secret page below.").pack()
        RouteLinkButton(self, "/secret", text="Go to Secret").pack(pady=5)
        RouteLinkButton(self, "/login", text="Login").pack(pady=5)


class LoginPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🔐 Login", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Button(self, text="Simulate Login", command=self.simulate_login).pack(pady=10)

    def simulate_login(self):
        global logged_in
        logged_in = True
        # Go to home, then navigate to secret to trigger guard check
        get_router().navigate("/")
        self.after(100, lambda: get_router().navigate("/secret"))


class SecretPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🎉 Secret Page", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="You will not see this page unless logged in").pack()
        RouteLinkButton(self, "/", text="Back to Home").pack(pady=10)


class AccessDeniedPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🚫 Access Denied", font=("Segoe UI", 18), foreground="red").pack(pady=10)
        RouteLinkButton(self, "/", text="Back to Home").pack(pady=10)


# --- Route configuration with guard ---

ROUTES = {
    "/": HomePage,
    "/login": LoginPage,
    "/secret": {
        "view": SecretPage,
        "guard": is_authenticated,
        "redirect": "/access-denied"
    },
    "/access-denied": AccessDeniedPage,
}


def run():
    root = tk.Tk()
    root.title("TkRouter – Route Guard Demo")
    root.geometry("480x300")
    ttk.Style().theme_use("clam")

    outlet = RouterOutlet(root)
    outlet.pack(fill="both", expand=True)

    create_router(ROUTES, outlet)
    get_router().navigate("/")

    root.mainloop()


if __name__ == "__main__":
    run()
