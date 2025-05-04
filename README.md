# TkRouter

A declarative routing system for building multi-page **Tkinter** applications with transitions, parameters, guards, and navigation history.

[Full documentation](https://tkrouter.readthedocs.io)

[![PyPI](https://img.shields.io/pypi/v/tkrouter)](https://pypi.org/project/tkrouter/)
[![License](https://img.shields.io/github/license/israel-dryer/tkrouter)](https://github.com/israel-dryer/tkrouter/blob/main/LICENSE)
---

## ✨ Features

* 🔀 Route matching with parameters (e.g., `/users/<id>`)
* ❓ Query string parsing (e.g., `/logs?level=info`)
* 🔄 Animated transitions (slide, fade)
* 🔒 Route guards with optional redirects
* 🧱 Singleton router via `create_router()` / `get_router()`
* 🧭 Navigation history: `.back()`, `.forward()`, `.go()`
* 📢 Route observers with `on_change()`
* 🧩 Routed widgets: `RouteLinkButton`, `RouteLinkLabel`
* 🎨 Works with `tk.Frame` or `ttk.Frame`

---

## 📦 Installation

```bash
pip install tkrouter
```

---

## 🚀 CLI Utilities

After installation, these command-line scripts become available:

```bash
tkrouter-create           # Generate a minimal main.py scaffold
tkrouter-demo-minimal     # Basic home/about demo
tkrouter-demo-admin       # Sidebar layout with query parameters
tkrouter-demo-unified     # Flat nested routes with transitions
tkrouter-demo-guarded     # Route guards with simulated login
```

---

## Quickstart

You can start a new Tkinter router-based app in two ways:

### 🚀 Option 1: Use the CLI

```bash
tkrouter-create
```

This generates a ready-to-run `main.py` file with a minimal working app.

---

### 🧪 Option 2: Use this snippet

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

## 🧪 Example Demos

```bash
python -m tkrouter.examples.minimal_app
python -m tkrouter.examples.admin_console
python -m tkrouter.examples.unified_routing
python -m tkrouter.examples.guarded_routes
```

| Example           | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `minimal_app`     | Basic Home/About router demo                                         |
| `admin_console`   | Sidebar UI with dynamic **routes** and **query parameters**          |
| `unified_routing` | Flat-style routing (e.g., `/dashboard/stats`) with slide transitions |
| `guarded_routes`  | Route guard demo with simulated login and redirect fallback          |

---

## 📚 API Overview

### Router Lifecycle

```python
create_router(routes: dict, outlet: RouterOutlet, transition_handler=None)
get_router() -> Router
```

### Route Config Format

```python
{
  "/users/<id>": {
    "view": UserDetailPage,
    "guard": is_logged_in,
    "redirect": "/login",
    "transition": slide_transition
  }
}
```

* Supports **dynamic route parameters** using angle brackets (e.g., `<id>`)
* Supports **query parameters** appended to URLs (e.g., `?tab=settings`)

### Transitions

```python
from tkrouter.transitions import slide_transition, simple_fade_transition
```

Set globally or per route config.

### Routed Widgets

* `RouteLinkButton(master, to, params=None, **kwargs)`
* `RouteLinkLabel(master, to, params=None, **kwargs)`
* `bind_route(widget, path, params=None)`
* `@with_route(path, params)` — for command binding

### Observing Route Changes

```python
get_router().on_change(lambda path, params: print("Route changed:", path, params))
```

---

## ⚠️ Exceptions

* `RouteNotFoundError` – Raised when no matching route is found
* `NavigationGuardError` – Raised when guard blocks navigation

---

## ✅ Compatibility

* Python 3.8 and newer

---

## 📄 License

MIT License © [Israel Dryer](https://github.com/israel-dryer/tkrouter)
