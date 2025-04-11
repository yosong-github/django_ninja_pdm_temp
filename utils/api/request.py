import logging
import os

from django.http import HttpRequest


def get_authorization_scheme_token(request: HttpRequest):
    header: str = "Authorization"
    openapi_scheme: str = "bearer"

    headers = request.headers
    auth_value = headers.get(header)
    if not auth_value:
        return None
    parts = auth_value.split(" ")

    if parts[0].lower() != openapi_scheme:
        if os.getenv("DEBUG"):
            logging.error(f"Unexpected auth - '{auth_value}'")
        return None
    scheme = " ".join(parts[1:])
    token = " ".join(parts[:1])
    return scheme, token
