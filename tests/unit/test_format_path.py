from tkrouter.widgets import format_path

def test_format_path_replaces_placeholders():
    path = "/user/<id>"
    params = {"id": 42}
    assert format_path(path, params) == "/user/42"

def test_format_path_appends_query_string():
    path = "/search"
    params = {"q": "python"}
    assert format_path(path, params) == "/search?q=python"

def test_format_path_combines_placeholders_and_query():
    path = "/user/<id>"
    params = {"id": 5, "view": "full"}
    assert format_path(path, params) == "/user/5?view=full"

def test_format_path_no_params_returns_original():
    path = "/static/page"
    assert format_path(path, None) == "/static/page"

def test_format_path_ignores_query_for_filled_placeholders():
    path = "/doc/<lang>"
    params = {"lang": "en", "mode": "dark"}
    assert format_path(path, params) == "/doc/en?mode=dark"
