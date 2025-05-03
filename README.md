> 🚧 **This project is in active development. Expect frequent changes and breaking updates.**
>
# TkRouter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/tkrouter.svg)](https://pypi.org/project/tkrouter/)

**TkRouter** brings declarative, animated routing to Tkinter, inspired by React Router and Angular Router.



## ✨ Features

- ✅ Simple route definitions with path-to-view mapping
- 🔁 Supports route transitions (slide, fade, etc.)
- 🛡️ Route guards and redirection
- 📦 Nested routes and 404 fallback handling
- 📜 URL parameter parsing (`/user/<id>`)
- 🧠 History stack (back/forward navigation)
- 🔗 Reusable navigation widgets (e.g., `RouteLinkButton`)
- 🎨 Theming-aware transitions

---

## 📦 Installation

Install TkRouter from PyPI:

```bash
pip install tkrouter
```

---

## 📚 Requirements

- Python 3.7+
- Tkinter (built-in on most systems)

---

## 🚀 Quick Start

```python
from tkrouter.router import Router
from tkrouter.route_view import RouteView
from examples.route_config import ROUTES

root = tk.Tk()
outlet = RouteView(root)
router = Router(routes=ROUTES, outlet=outlet)
router.navigate("/")  # Shows the HomePage
```

---

## 📁 Route Configuration

```python
ROUTES = {
    "/": HomePage,
    "/about": {
        "view": AboutPage,
        "transition": slide_transition
    },
    "*": NotFoundPage
}
```

---

## 🔧 Transitions

Use built-in transitions or create your own:

```python
from tkrouter.transitions import slide_transition, simple_fade_transition
```

---

## 📂 Example Project Structure

This is what an end-user project might look like when using TkRouter:

```
examples/
├── views.py             # Page components (HomePage, AboutPage, etc.)
├── route_config.py      # All route declarations
└── basic_app.py         # Main application entry point
```

---

## 🧪 Testing

```bash
pytest tests/
```


---

## 🧪 Try It Locally

```bash
git clone https://github.com/israel-dryer/tkrouter.git
cd tkrouter/examples
python basic_app.py
```

## 📄 License

MIT License


---

## 🎥 Demo

![TkRouter Demo](docs/demo.gif)

> The above shows animated navigation between views using slide and fade transitions.

---

## 🖼️ Screenshots

| Home Page         | About Page        | 404 Fallback       |
|-------------------|-------------------|--------------------|
| ![Home](docs/home.png) | ![About](docs/about.png) | ![404](docs/404.png) |


## 🌲 Nested Routing

TkRouter supports nested routes via the `children` property.

Use `ChildRouteView` in your parent view to render the active child:

```python
ROUTES = {
    "/settings": {
        "view": SettingsPage,
        "children": {
            "/profile": {
                "view": ProfilePage,
                "children": {
                    "/details": ProfileDetailsPage
                }
            },
            "/account": AccountPage
        }
    }
}
```

In `SettingsPage`:

```python
self.child_view = ChildRouteView(self, master.router, "/settings")
self.child_view.pack(fill="both", expand=True)
```

In `ProfilePage` (to render `/settings/profile/details`):

```python
self.child_view = ChildRouteView(self, master.router, "/settings/profile")
self.child_view.pack(fill="both", expand=True)
```


## 🔣 Route Parameters

TkRouter supports dynamic route segments using angle brackets:

```python
ROUTES = {
    "/user/<id>": UserProfilePage
}
```

In your view, define an `on_navigate()` method to access parameters:

```python
class UserProfilePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self)
        self.label.pack()

    def on_navigate(self, params):
        user_id = params.get("id", "unknown")
        self.label.config(text=f"User ID: {user_id}")
```
