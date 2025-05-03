import time
import tkinter as tk

def slide_transition(outlet, view_class, params, duration=300):
    if outlet.current_view:
        outlet.current_view.place_forget()
        outlet.current_view.destroy()

    new_view = view_class(outlet)
    width = outlet.winfo_width()
    new_view.place(x=width, y=0, relheight=1, width=width)
    outlet.current_view = new_view

    if hasattr(new_view, 'on_enter'):
        new_view.on_enter(params)

    def animate():
        start = time.time()

        def step():
            progress = min(1, (time.time() - start) * 1000 / duration)
            x = int(width * (1 - progress))
            new_view.place(x=x, y=0)
            if progress < 1:
                outlet.after(16, step)
            else:
                new_view.place(x=0, y=0)
                new_view.pack(fill="both", expand=True)
                new_view.place_forget()

        step()

    animate()


def get_background_color(widget):
    try:
        return widget.cget("background")
    except Exception:
        return "#ffffff"

def is_dark(color):
    try:
        rgb = widget.winfo_rgb(color)
        brightness = (rgb[0] + rgb[1] + rgb[2]) / (65535 * 3)
        return brightness < 0.5
    except Exception:
        return False

def simple_fade_transition(outlet, view_class, params, duration=300):
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
    fade_color = "#000000" if is_dark(bg_color) else "#ffffff"

    fade_overlay = tk.Frame(outlet, bg=fade_color)
    fade_overlay.place(x=0, y=0, relwidth=1, relheight=1)
    fade_overlay.lift()

    def fade_out(step=steps):
        alpha = int((step / steps) * 255)
        color = fade_color
        fade_overlay.configure(bg=color)
        if step > 0:
            outlet.after(delay, lambda: fade_out(step - 1))
        else:
            fade_overlay.destroy()
            new_view.pack(fill="both", expand=True)

    fade_out()
