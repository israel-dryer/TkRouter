import pytest
from tkrouter.history import History


def test_push():
    history = History()
    history.push("/home")
    assert history.size == 1
    assert history.current() == "/home"


def test_back():
    history = History()
    history.push("/home")
    history.push("/about")
    assert history.back() == "/home"
    assert history.current() == "/home"


def test_forward():
    history = History()
    history.push("/home")
    history.push("/about")
    history.back()
    assert history.forward() == "/about"
    assert history.current() == "/about"


def test_go():
    history = History()
    history.push("/home")
    history.push("/about")
    history.push("/contact")
    
    assert history.go(-1) == "/about"  # Navigate back one step
    assert history.current() == "/about"
    
    assert history.go(-2) is None  # Go out of bounds (too far back), returns None
    assert history.current() == "/about"  # Current position remains unchanged

    assert history.go(2) is None  # Go out of bounds (too far forward), returns None
    assert history.current() == "/about"


def test_go_out_of_bounds():
    history = History()
    history.push("/home")
    history.push("/about")
    history.push("/contact")
    
    # Going out of bounds backward
    assert history.go(-10) is None  # Too far back
    assert history.current() == "/contact"  # Current state remains unchanged

    # Going out of bounds forward
    assert history.go(10) is None  # Too far forward
    assert history.current() == "/contact"  # Current state remains unchanged


def test_replace():
    history = History()
    history.push("/home")
    history.replace("/new_home")
    assert history.current() == "/new_home"


def test_replace_on_empty_stack_raises_error():
    history = History()
    with pytest.raises(IndexError):
        history.replace("/new_home")  # No item to replace


def test_clear():
    history = History()
    history.push("/home")
    history.push("/about")
    history.clear()
    assert history.size == 0
    assert history.current() is None


def test_can_go_back_and_forward():
    history = History()
    assert not history.can_go_back
    assert not history.can_go_forward

    history.push("/home")
    assert not history.can_go_back
    assert not history.can_go_forward

    history.push("/about")
    assert history.can_go_back
    assert not history.can_go_forward

    history.back()
    assert not history.can_go_back
    assert history.can_go_forward

    history.forward()
    assert history.can_go_back
    assert not history.can_go_forward


def test_push_resets_forward_history():
    history = History()
    history.push("/home")
    history.push("/about")
    history.back()
    history.push("/contact")  # Should reset forward history
    assert history.size == 2  # "/contact" replaces everything after the current index
    assert history.current() == "/contact"
    assert not history.can_go_forward