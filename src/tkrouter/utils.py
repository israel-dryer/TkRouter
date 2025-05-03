from urllib.parse import parse_qs, urlparse

def format_path(path, params):
    """Fill placeholders and append query params."""
    if not params:
        return path

    path_filled = path
    query_items = {}
    for key, val in params.items():
        if f"<{key}>" in path:
            path_filled = path_filled.replace(f"<{key}>", str(val))
        else:
            query_items[key] = val

    if query_items:
        path_filled += "?" + "&".join(f"{k}={v}" for k, v in query_items.items())

    return path_filled

def strip_query(path):
    """Return path without query string."""
    return path.split("?")[0]

def extract_query_params(path):
    """Return query params as a dict from full path."""
    return {k: v[0] for k, v in parse_qs(urlparse(path).query).items()}

def normalize_route_config(config):
    """Ensure all routes have a dict with a view key."""
    if isinstance(config, dict):
        return config
    return {"view": config}
