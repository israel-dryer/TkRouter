import tkinter as tk
from src.tkrouter.link_widgets import RouteLinkButton

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Home Page").pack()
        RouteLinkButton(self, master.router, "/about", text="Go to About").pack()

class AboutPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="About Page").pack()
        RouteLinkButton(self, master.router, "/", text="Back Home").pack()

class NotFoundPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="404 - Not Found").pack()
