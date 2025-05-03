from examples.views import UserProfilePage, ProfileDetailsPage, HomePage, AboutPage, LoginPage, NotFoundPage, SettingsPage, ProfilePage, AccountPage
from tkrouter.transitions import slide_transition, simple_fade_transition

ROUTES = {
    "/": HomePage,
    "/about": {
        "view": AboutPage,
        "transition": slide_transition
    },
    "/login": {
        "view": LoginPage,
        "transition": simple_fade_transition
    },
    "/settings": {
        "view": SettingsPage,
        "children": {
            "/profile": {
                "view": ProfilePage,
                "children": {
                    "/details": ProfileDetailsPage
                }
            },
            "/account": AccountPage
        }
    },
    "/user/<id>": UserProfilePage,
    "*": NotFoundPage
}
