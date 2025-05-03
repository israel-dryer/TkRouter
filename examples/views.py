import tkinter as tk
from tkrouter.link_widgets import RouteLinkButton
from tkrouter.child_route_view import ChildRouteView


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Home Page").pack()
        RouteLinkButton(self, master.router, "/about", text="Go to About").pack()
        RouteLinkButton(self, master.router, "/nonexistent", text="Invalid Route").pack()
        RouteLinkButton(self, master.router, "/user/123", text="Go to User 123").pack()
        RouteLinkButton(self, master.router, "/search?term=tkrouter&page=2", text="Search tkrouter (Page 2)").pack()

class SearchPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self)
        self.label.pack()

    def on_navigate(self, params):
        term = params.get("term", "(no term)")
        page = params.get("page", "1")
        self.label.config(text=f"Search: '{term}', Page: {page}")

class UserProfilePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self)
        self.label.pack()

    def on_navigate(self, params):
        user_id = params.get("id", "unknown")
        self.label.config(text=f"User ID: {user_id}")

class AboutPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="About Page").pack()
        RouteLinkButton(self, master.router, "/", text="Back Home").pack()
        self.back_btn = tk.Button(self, text="⬅ Back", command=self.back_nav)
        self.back_btn.pack()
        self.forward_btn = tk.Button(self, text="➡ Forward", command=self.forward_nav)
        self.forward_btn.pack()
        self.after(100, self.check_nav_state)

    def back_nav(self):
        if self.master.router:
            self.master.router.back()

    def forward_nav(self):
        if self.master.router:
            self.master.router.forward()

    def check_nav_state(self):
        history = self.master.router.history
        can_back = history._index > 0
        can_forward = history._index + 1 < len(history._stack)
        self.back_btn.config(state=tk.NORMAL if can_back else tk.DISABLED)
        self.forward_btn.config(state=tk.NORMAL if can_forward else tk.DISABLED)
        self.after(250, self.check_nav_state)


class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Login Page").pack()


class SettingsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Settings").pack()
        RouteLinkButton(self, master.router, "/settings/profile", text="Profile").pack()
        RouteLinkButton(self, master.router, "/settings/account", text="Account").pack()
        self.child_view = ChildRouteView(self, master.router, "/settings")
        self.child_view.pack(fill="both", expand=True)

class ProfilePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Profile Settings").pack()
        RouteLinkButton(self, master.router, "/settings/profile/details", text="Details").pack()
        self.child_view = ChildRouteView(self, master.router, "/settings/profile")
        self.child_view.pack(fill="both", expand=True)


class AccountPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Account Settings").pack()

class ProfileDetailsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Profile → Details").pack()

class NotFoundPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="404 - Page Not Found").pack()
