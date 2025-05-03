> 🚧 **This project is in active development. Expect frequent changes and breaking updates.**
>
# TkRouter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/tkrouter.svg)](https://pypi.org/project/tkrouter/)

**TkRouter** brings declarative, animated routing to Tkinter, inspired by React Router and Angular Router.

---

## ✨ Features

- ✅ Simple route definitions with path-to-view mapping
- 🔁 Supports route transitions (slide, fade, etc.)
- 🛡️ Route guards and redirection
- 📦 Nested routes and 404 fallback handling
- 📜 URL and query parameter parsing (`/user/<id>?sort=asc`)
- 🧠 History stack (back/forward navigation)
- 🔗 Reusable navigation widgets (e.g., `RouteLinkButton`)
- 🧭 Route observers (`on_change()`)
- 🎨 Theming-aware transitions

---

## 📦 Installation

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

## 🔣 Route Parameters

Dynamic segments use angle brackets:

```python
ROUTES = {
    "/user/<id>": UserProfilePage
}
```

In your view:

```python
class UserProfilePage(tk.Frame):
    def on_navigate(self, params):
        user_id = params.get("id")
```

---

## ❓ Query Parameters

Query parameters are parsed automatically and merged with route parameters.

```python
/search?term=tkrouter&page=2
```

```python
class SearchPage(tk.Frame):
    def on_navigate(self, params):
        term = params.get("term")
        page = params.get("page")
```

---

## 🌲 Nested Routing

TkRouter supports nested routes via the `children` property.

```python
ROUTES = {
    "/settings": {
        "view": SettingsPage,
        "children": {
            "/profile": ProfilePage,
            "/account": AccountPage
        }
    }
}
```

In your view:

```python
self.child_view = ChildRouteView(self, master.router, "/settings")
self.child_view.pack(fill="both", expand=True)
```

---

## 🔗 Navigation Widgets

TkRouter includes reusable helpers and widgets to simplify routing in your app.

### `RouteLinkButton`

```python
RouteLinkButton(self, router, "/user/<id>", params={"id": 42}, text="Go to User 42")
```

### `with_route()` - Decorator or Inline Command

Use as a decorator:

```python
@with_route(router, "/login")
def login_handler():
    ...
```

Or attach as a button command with dynamic params:

```python
tk.Button(self, text="Go", command=with_route(router, "/search", params={"term": "python"}))
```

### `bind_route()` - Attach to Any Widget

```python
label = tk.Label(self, text="Go to Home")
bind_route(label, router, "/", params={"from": "label"})
```

This allows any widget to act as a navigation trigger with optional parameters.

## 🧭 Route Observers

Track route changes in real-time:

```python
router.on_change(lambda path, params: print("Navigated to:", path, params))
```

Useful for:
- Analytics and logging
- Window title updates
- State syncing

---

## 📂 Example Project Structure

```
examples/
├── views.py             # Page components
├── route_config.py      # Routes definition
└── basic_app.py         # App entry point
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

---

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