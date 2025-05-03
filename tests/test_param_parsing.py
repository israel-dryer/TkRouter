from src.tkrouter.router import Router

class DummyOutlet:
    def set_view(self, view_class, params):
        self.params = params

class DummyView:
    def __init__(self, master):
        self.master = master


def test_dynamic_parameter_parsing():
    outlet = DummyOutlet()
    router = Router(routes={"/user/<id>": DummyView}, outlet=outlet)
    router.navigate("/user/42")
    assert outlet.params["id"] == "42"


def test_multiple_parameters():
    outlet = DummyOutlet()
    router = Router(routes={"/order/<order_id>/item/<item_id>": DummyView}, outlet=outlet)
    router.navigate("/order/123/item/abc")
    assert outlet.params["order_id"] == "123"
    assert outlet.params["item_id"] == "abc"


def test_parameter_with_nested_route():
    outlet = DummyOutlet()
    routes = {
        "/dashboard": {
            "view": DummyView,
            "children": {
                "/user/<uid>": DummyView
            }
        }
    }
    router = Router(routes=routes, outlet=outlet)
    router.navigate("/dashboard/user/alice")
    assert outlet.params["uid"] == "alice"
