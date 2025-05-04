from urllib.parse import parse_qs, urlparse
from typing import Dict, Any


def format_path(path: str, params: Dict[str, Any]) -> str:
    """
    Formats a route path by substituting dynamic segments and appending query parameters.

    Args:
        path (str): The base route, e.g. "/users/<id>".
        params (dict): Parameters to insert into path or append as query parameters.

    Returns:
        str: The formatted path with placeholders replaced and query parameters appended.

    Example:
        format_path("/users/<id>", {"id": 5, "tab": "profile"})
        → "/users/5?tab=profile"
    """
    if not params:
        return path

    path_filled = path
    query_items = {}

    for key, val in params.items():
        placeholder = f"<{key}>"
        if placeholder in path_filled:
            path_filled = path_filled.replace(placeholder, str(val))
        else:
            query_items[key] = val

    if query_items:
        query_string = "&".join(f"{k}={v}" for k, v in query_items.items())
        path_filled += "?" + query_string

    return path_filled


def strip_query(path: str) -> str:
    """
    Removes the query string from a path.

    Args:
        path (str): A full path that may include a query string.

    Returns:
        str: The base path without query parameters.

    Example:
        "/users/5?tab=profile" → "/users/5"
    """
    return path.split("?")[0]


def extract_query_params(path: str) -> Dict[str, str]:
    """
    Extracts query parameters from a path string.

    Args:
        path (str): A full path with optional query string.

    Returns:
        dict: A dictionary of query parameters. Values are decoded strings.

    Example:
        "/users?id=5&tab=info" → {"id": "5", "tab": "info"}
    """
    return {k: v[0] for k, v in parse_qs(urlparse(path).query).items()}


def normalize_route_config(config: Any) -> Dict[str, Any]:
    """
    Normalizes a route config to always return a dictionary with a 'view' key.

    Args:
        config (dict or object): The route config, which may be a plain view class.

    Returns:
        dict: A config dictionary with at least a 'view' key.

    Example:
        normalize_route_config(MyViewClass) → {"view": MyViewClass}
    """
    if isinstance(config, dict):
        return config
    return {"view": config}
