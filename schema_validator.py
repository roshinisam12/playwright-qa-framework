import jsonschema


USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id":       {"type": "integer"},
        "name":     {"type": "string"},
        "username": {"type": "string"},
        "email":    {"type": "string", "format": "email"},
        "phone":    {"type": "string"},
        "website":  {"type": "string"},
    }
}

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id":     {"type": "integer"},
        "userId": {"type": "integer"},
        "title":  {"type": "string"},
        "body":   {"type": "string"},
    }
}


def validate_schema(data: dict, schema: dict):
    """Validate a response body against a JSON schema. Raises AssertionError on failure."""
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")
