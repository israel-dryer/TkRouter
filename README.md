# TkRouter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)

**TkRouter** brings declarative, animated routing to Tkinter, inspired by React Router and Angular Router.


**TkRouter** is a lightweight, declarative routing and navigation library for Python's Tkinter framework—designed to bring the power of React Router and Angular Router into desktop GUI development.

---

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

`pip install tkrouter`

For now, clone the repo:

```bash
git clone https://github.com/israel-dryer/tkrouter.git
cd TkRouter
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

This is what a project might look like when using TkRouter:

```
example_app/
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
