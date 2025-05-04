import time
import tkinter as tk


def slide_transition(outlet, view_class, params, duration=300):
    """
    Performs a horizontal slide transition for view changes.

    The new view slides in from the right over the current view. If `on_enter`
    is defined on the view class, it will be called with the provided `params`.

    Args:
        outlet (tk.Frame): The container managing the current and new views.
        view_class (type): The class of the new view to be shown.
        params (dict): Parameters to pass to the view's `on_enter()` method.
        duration (int): Duration of the animation in milliseconds (default: 300).
    """
    if outlet.current_view:
        outlet.current_view.place_forget()
        outlet.current_view.destroy()

    width = outlet.winfo_width()
    new_view = view_class(outlet)
    new_view.place(x=width, y=0, relheight=1, width=width)
    outlet.current_view = new_view

    if hasattr(new_view, 'on_enter'):
        new_view.on_enter(params)

    def animate():
        start = time.time()

        def step():
            elapsed = time.time() - start
            progress = min(1, elapsed * 1000 / duration)
            x = int(width * (1 - progress))
            new_view.place(x=x, y=0)
            if progress < 1:
                outlet.after(16, step)
            else:
                new_view.place_forget()
                new_view.pack(fill="both", expand=True)

        step()

    animate()


def simple_fade_transition(outlet, view_class, params, duration=300):
    """
    Fades from the current view to a new view using an overlay.

    A full-frame overlay is created and gradually faded out, revealing the new view.
    If the new view has `on_enter(params)`, it will be called.

    Args:
        outlet (tk.Frame): The container managing the view stack.
        view_class (type): Class of the new view to be instantiated.
        params (dict): Parameters to pass to `on_enter()`, if defined.
        duration (int): Duration of the fade in milliseconds (default: 300).
    """
    steps = 20
    delay = int(duration / steps)

    if outlet.current_view:
        outlet.current_view.destroy()

    new_view = view_class(outlet)
    new_view.place(x=0, y=0, relwidth=1, relheight=1)
    outlet.current_view = new_view

    if hasattr(new_view, 'on_enter'):
        new_view.on_enter(params)

    bg_color = get_background_color(outlet)
    fade_color = "#000000" if is_dark(outlet, bg_color) else "#ffffff"

    overlay = tk.Frame(outlet, bg=fade_color)
    overlay.place(x=0, y=0, relwidth=1, relheight=1)
    overlay.lift()

    def fade_out(step=steps):
        if step > 0:
            overlay.after(delay, lambda: fade_out(step - 1))
        else:
            overlay.destroy()
            new_view.pack(fill="both", expand=True)

    fade_out()


def get_background_color(widget):
    """
    Attempts to retrieve the background color of a widget.

    Args:
        widget (tk.Widget): The widget to inspect.

    Returns:
        str: The background color, or '#ffffff' as a fallback.
    """
    try:
        return widget.cget("background")
    except Exception:
        return "#ffffff"


def is_dark(widget, color):
    """
    Heuristic to determine if a color is dark based on brightness.

    Args:
        widget (tk.Widget): Any Tkinter widget for color resolution.
        color (str): A color name or hex string (e.g. '#333333').

    Returns:
        bool: True if the color is dark; False otherwise.
    """
    try:
        r, g, b = widget.winfo_rgb(color)
        brightness = (r + g + b) / (65535 * 3)
        return brightness < 0.5
    except Exception:
        return False
