# TkRouter

A declarative routing system for building multi-page **Tkinter** applications with transitions, parameters, guards, and history navigation.

![PyPI](https://img.shields.io/pypi/v/tkrouter) ![License](https://img.shields.io/github/license/israel-dryer/tkrouter)

---

## ✨ Features

- 🔀 **Route matching** with support for parameters (e.g., `/users/<id>`)
- ❓ **Query string parsing** (e.g., `/logs?level=info`)
- 🔄 **Animated transitions** (`slide`, `fade`) between views
- 🧱 **Singleton router API** with `create_router()` and `get_router()`
- 🔒 **Route guards** with optional redirect fallback
- 🧭 **History stack** with `.back()`, `.forward()`, `.go()`
- 🧩 **Routed widgets** like `RouteLinkButton`, `RouteLinkLabel`
- 🎨 Works with both `tk.Frame` and `ttk.Frame` subclasses

---

## 📦 Installation

```bash
pip install tkrouter
```

---

## 🧭 Quickstart

Use the `tkrouter-create` command in your terminal to stand up a minimal starting app, or use the snippet below:

```python
from tkinter import Tk
from tkrouter import create_router, get_router, RouterOutlet
from tkrouter.views import RoutedView
from tkrouter.widgets import RouteLinkButton

class Home(RoutedView):
    def __init__(self, master):
        super().__init__(master)
        RouteLinkButton(self, "/about", text="Go to About").pack()

class About(RoutedView):
    def __init__(self, master):
        super().__init__(master)
        RouteLinkButton(self, "/", text="Back to Home").pack()

ROUTES = {
    "/": Home,
    "/about": About,
}

root = Tk()
outlet = RouterOutlet(root)
outlet.pack(fill="both", expand=True)
create_router(ROUTES, outlet).navigate("/")
root.mainloop()
```

---

## 🧪 Examples

Run any of these from the project root using Python's module runner:

```bash
python -m tkrouter.examples.minimal_app
python -m tkrouter.examples.admin_console
python -m tkrouter.examples.unified_routing
python -m tkrouter.examples.guarded_routes
```

| File              | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| `minimal_app`     | A basic home/about router demo                                      |
| `admin_console`   | Sidebar layout with dynamic routes and query params                 |
| `unified_routing` | Flat path routing (`/dashboard/stats`) with transitions             |
| `guarded_routes`  | Simulated login with protected `/secret` view and redirect fallback |

---

## 📚 API Overview

### Routing

```python
create_router(routes: dict, outlet: RouterOutlet, transition_handler=None)
get_router() -> Router
```

### Route Configs

```python
{
  "/users/<id>": {
    "view": UserDetailsPage,
    "guard": is_authenticated,     # optional
    "redirect": "/login",          # optional
    "transition": slide_transition # optional
  }
}
```

### Widgets

- `RouteLinkButton(master, to: str, params: dict = None, **kwargs)`
- `RouteLinkLabel(master, to: str, params: dict = None, **kwargs)`
- `bind_route(widget, path, params)`
- `with_route(path, params)(func)` – decorator for route-bound handlers

---

## 🔄 Transitions

Available transitions:

```python
from tkrouter.transitions import slide_transition, simple_fade_transition
```

You can also define your own with the signature:

```python
def my_transition(outlet, view_class, params, duration=300): ...
```

---

## ⚠️ Exceptions

```python
from tkrouter.exceptions import RouteNotFoundError, NavigationGuardError
```

---

## ✅ Supported Python Versions

- Python 3.8+

---

## 🚀 CLI Scripts

Once installed from PyPI, these scripts will be available in your terminal:

```bash
tkrouter-create           # Generate a minimal main.py app scaffold
tkrouter-demo-minimal     # Minimal Home/About app
tkrouter-demo-admin       # Full sidebar admin layout with query params
tkrouter-demo-unified     # Unified flat routes with transitions
tkrouter-demo-guarded     # Route guard with simulated login
```

---

## 📄 License

MIT © Israel Dryer  
[github.com/israel-dryer/tkrouter](https://github.com/israel-dryer/tkrouter)

---
