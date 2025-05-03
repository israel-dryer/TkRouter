import tkinter as tk
from src.tkrouter.router import Router
from src.tkrouter.route_view import RouteView
from examples.route_config import ROUTES

root = tk.Tk()
root.geometry("300x200")

outlet = RouteView(root)
outlet.pack(fill="both", expand=True)

router = Router(routes=ROUTES, outlet=outlet)
outlet.router = router

# Try navigating to an invalid route
router.navigate("/nonexistent")  # should load NotFoundPage

root.mainloop()
