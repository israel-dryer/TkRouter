from examples.views import HomePage, AboutPage, NotFoundPage
from src.tkrouter.transitions import slide_transition

ROUTES = {
    "/": HomePage,  # simple format
    "/about": {     # extended format
        "view": AboutPage,
        "transition": slide_transition
    },
    "*": NotFoundPage
}
