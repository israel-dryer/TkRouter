import tkinter as tk
from tkrouter.router import Router
from tkrouter.route_view import RouteView
from examples.route_config import ROUTES

root = tk.Tk()
root.geometry("300x200")

outlet = RouteView(root)
outlet.pack(fill="both", expand=True)

router = Router(routes=ROUTES, outlet=outlet)
outlet.router = router
router.navigate("/")  # Shows the HomePage

root.mainloop()
