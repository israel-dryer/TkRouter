# API Reference

## 🔧 Router Lifecycle

### create_router

```python
create_router(routes: dict, outlet: RouterOutlet, transition_handler: Optional[Callable] = None) -> Router
```
Creates and registers the global singleton Router instance.

- `routes`: A dictionary mapping paths to view classes or route configs
- `outlet`: The RouterOutlet container where views render
- `transition_handler`: Optional fallback transition function

#### Example

```python
create_router(ROUTES, outlet)
```

Initializes the global router with your route map and main outlet container.

---

### get_router

```python
get_router() -> Router
```
Returns the globally registered Router.  
Raises `RuntimeError` if `create_router()` hasn’t been called.

#### Example

```python
router = get_router()
```

Retrieves the global router instance. Useful for navigating or registering listeners.

---

## 📦 Router Methods

### navigate

```python
navigate(path: str, transition: Optional[Callable] = None)
```
Navigates to a route. Handles parameters, query strings, guards, transitions, and history.

#### Example

```python
get_router().navigate("/users/42?tab=profile")
```

---

### back

```python
back()
```
Navigates to the previous route in the history stack.

---

### forward

```python
forward()
```
Navigates forward in the history stack.

---

### go

```python
go(delta: int)
```
Navigates by a relative offset (e.g., -1 to go back, 1 to go forward).

---

### on_change

```python
on_change(callback: Callable[[str, dict], None])
```
Registers a listener to respond to route changes.

#### Example

```python
get_router().on_change(lambda path, params: print("Route changed:", path))
```

---

## 🗺️ Route Config Format

```python
ROUTES = {
    "/": HomePage,
    "/about": AboutPage,
    "/users/<id>": {
        "view": UserDetailPage,
        "guard": is_logged_in,
        "redirect": "/login",
        "transition": slide_transition
    }
}
```
Supports dynamic segments (`<id>`), route guards, custom transitions, and redirects.

---

## 🎛️ Routed Widgets

### RouteLinkButton

```python
RouteLinkButton(master, to: str, params: dict = None, **kwargs)
```
A button that navigates to a route when clicked.

#### Example

```python
RouteLinkButton(self, "/about", text="Go to About")
```

---

### RouteLinkLabel

```python
RouteLinkLabel(master, to: str, params: dict = None, **kwargs)
```
A label that acts like a hyperlink and navigates on click.

#### Example

```python
RouteLinkLabel(self, "/users/<id>", params={"id": 12}, text="User 12")
```

---

### bind_route

```python
bind_route(widget, path: str, params: dict = None)
```
Binds navigation logic to any widget with a `command` option.

#### Example

```python
bind_route(my_button, "/settings", params={"tab": "advanced"})
```

---

### with_route

```python
@with_route(path, params)
def handler(): ...
```
Decorator that adds route metadata to a function.

#### Example

```python
@with_route("/help")
def open_help():
    ...
```

---

## 🎥 Transitions

### slide_transition

```python
slide_transition(outlet, view_class, params, duration=300)
```
Animates a slide-in transition from the right.

#### Example

```python
from tkrouter.transitions import slide_transition
create_router(ROUTES, outlet, transition_handler=slide_transition)
```

---

### simple_fade_transition

```python
simple_fade_transition(outlet, view_class, params, duration=300)
```
Fades between views using an overlay.

#### Example

```python
from tkrouter.transitions import simple_fade_transition
ROUTES = {
    "/fade": {
        "view": FadeView,
        "transition": simple_fade_transition
    }
}
```

---

## ⚠️ Exceptions

### RouteNotFoundError

Raised when no route matches the requested path.

### NavigationGuardError

Raised when a guard condition blocks access to a route.