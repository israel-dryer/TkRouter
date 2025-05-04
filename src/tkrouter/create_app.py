import os

MINIMAL_APP_CODE = """import tkinter as tk
from tkinter import ttk
from tkrouter import create_router, get_router
from tkrouter.router_outlet import RouterOutlet
from tkrouter.views import StyledRoutedView
from tkrouter.widgets import RouteLinkButton

class HomePage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="🏠 Home", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="Welcome to your TkRouter app!").pack()
        RouteLinkButton(self, "/about", text="Go to About").pack(pady=10)

class AboutPage(StyledRoutedView):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text="ℹ️ About", font=("Segoe UI", 18)).pack(pady=10)
        ttk.Label(self, text="This is a minimal routed app.").pack()
        RouteLinkButton(self, "/", text="Back to Home").pack(pady=10)

ROUTES = {
    "/": HomePage,
    "/about": AboutPage,
}

def main():
    root = tk.Tk()
    root.title("My TkRouter App")
    root.geometry("400x250")

    style = ttk.Style()
    style.theme_use("clam")

    outlet = RouterOutlet(root)
    outlet.pack(fill="both", expand=True)

    create_router(ROUTES, outlet)
    get_router().navigate("/")

    root.mainloop()

if __name__ == "__main__":
    main()
"""

def create_main_py():
    if os.path.exists("main.py"):
        print("main.py already exists. Aborting.")
        return

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(MINIMAL_APP_CODE)
        print("✅ Created main.py with a minimal TkRouter app.")

if __name__ == "__main__":
    create_main_py()