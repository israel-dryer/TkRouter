# TkRouter

**TkRouter** is a declarative routing system for building multi-page **Tkinter** applications. It supports parameterized routes, query strings, animated transitions, history navigation, and more.

![PyPI](https://img.shields.io/pypi/v/tkrouter)
![License](https://img.shields.io/github/license/israel-dryer/tkrouter)

---

## ✨ Features

- 🔀 Route matching with **parameters** (`/users/<id>`)
- ❓ **Query string** parsing (`/logs?level=debug`)
- 🔄 Animated **transitions** between views (`slide`, `fade`)
- 🧭 Singleton **router instance** (`create_router()`, `get_router()`)
- 🔐 Route **guards** with redirect support
- ⏪ History **navigation** (`.back()`, `.forward()`, `.go()`)
- 🧩 Built-in **widgets**: `RouteLinkButton`, `RouteLinkLabel`
- 🎨 Compatible with both `tk.Frame` and `ttk.Frame`

---

## 📦 Installation

```bash
pip install tkrouter
```

---

## 🚀 Quickstart

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

Run these from the terminal (installed via `pip`) or with `python -m tkrouter.examples.NAME`.

| Script                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `tkrouter-demo-minimal`  | Basic two-page example                                                      |
| `tkrouter-demo-admin`    | Sidebar layout with query param routing (`/logs?level=error`)               |
| `tkrouter-demo-unified`  | Flat URL routes (`/dashboard/stats`) with transitions                      |
| `tkrouter-demo-guarded`  | Simulated login with protected route and redirect (`/secret → /login`)      |

---

## 🧭 Route Config

```python
ROUTES = {
    "/": HomePage,
    "/users/<id>": {
        "view": UserDetailPage,
        "transition": slide_transition,
        "guard": is_logged_in,
        "redirect": "/login"
    }
}
```

✅ Supports:

- `<id>` dynamic parameters
- `?key=value` query parameters
- Route guards and redirects
- Per-route transitions

---

## 🧱 Router API

```python
from tkrouter import create_router, get_router

router = create_router(routes, outlet)
router.navigate("/users/123?tab=details")
router.back()
router.on_change(lambda path, params: print(path, params))
```

---

## 🧩 Routed Widgets

```python
from tkrouter.widgets import RouteLinkButton, RouteLinkLabel

RouteLinkButton(parent, "/dashboard")
RouteLinkLabel(parent, "/users/<id>", params={"id": 3})
```

Also available:

- `bind_route(widget, path, params)`
- `@with_route(path, params)` decorator

---

## 🔄 Transitions

```python
from tkrouter.transitions import slide_transition, simple_fade_transition
```

Custom transitions supported — just pass a function like:

```python
def my_transition(outlet, view_class, params, duration=300): ...
```

---

## ⚠️ Exceptions

```python
from tkrouter.exceptions import RouteNotFoundError, NavigationGuardError
```

---

## ✅ Compatibility

- Python 3.8+

---

## 📄 License

MIT © [Israel Dryer](https://github.com/israel-dryer/tkrouter)

---