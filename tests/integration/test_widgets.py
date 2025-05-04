import pytest
import tkinter as tk

try:
    root_test = tk.Tk()
    root_test.destroy()
except tk.TclError:
    pytest.skip("Tkinter not supported in this environment", allow_module_level=True)

import tkinter as tk
import pytest
from unittest.mock import Mock
from tkrouter.widgets import RouteLinkButton, bind_route, with_route

@pytest.fixture
def mock_router():
    """
    Fixture to create a mock router for testing.

    Returns:
        Mock: A mock object simulating a router.
    """
    return Mock()

def test_route_link_button_navigates_with_params(mock_router):
    """
    Test that the RouteLinkButton correctly navigates to the specified route with parameters.

    Args:
        mock_router (Mock): A mock router object for navigation.

    Raises:
        AssertionError: If navigation is not called with the expected route.
    """
    root = tk.Tk()
    button = RouteLinkButton(root, mock_router, "/test/<x>", params={"x": 1})
    button.invoke()
    mock_router.navigate.assert_called_with("/test/1")
    root.destroy()

def test_bind_route_navigates_with_query(mock_router):
    """
    Test that the bind_route function attaches a navigation command that includes query parameters.

    Args:
        mock_router (Mock): A mock router object for navigation.

    Raises:
        AssertionError: If the navigation command is not called with the expected route.
    """
    root = tk.Tk()
    btn = tk.Button(root)
    bind_route(btn, mock_router, "/search", params={"q": "book"})
    btn.invoke()
    mock_router.navigate.assert_called_with("/search?q=book")
    root.destroy()

def test_with_route_decorator_sets_metadata(mock_router):
    """
    Test that the with_route decorator correctly attaches routing metadata to functions.

    Args:
        mock_router (Mock): A mock router object for navigation.

    Raises:
        AssertionError: If the decorated function does not produce the expected output or metadata.
    """
    @with_route(mock_router, "/hello/<lang>", params={"lang": "en"})
    def test_func():
        """
        A test function decorated with routing metadata.

        Returns:
            str: A sample return value for testing.
        """
        return "Hello"

    result = test_func()
    assert result == "Hello"
    assert hasattr(test_func, "_router_path")
    assert test_func._router_path == "/hello/en"
    assert test_func._router == mock_router