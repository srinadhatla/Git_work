from rest_framework.views import exception_handler

from rest_framework.exceptions import (
    ValidationError,
    AuthenticationFailed,
    PermissionDenied,
    NotFound
)


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        return response

    if isinstance(exc, ValidationError):

        response.data = {
            "success": False,
            "message": "Validation Error",
            "errors": response.data
        }

    elif isinstance(exc, AuthenticationFailed):

        response.data = {
            "success": False,
            "message": "Authentication Failed",
            "errors": response.data
        }

    elif isinstance(exc, PermissionDenied):

        response.data = {
            "success": False,
            "message": "Permission Denied",
            "errors": response.data
        }

    elif isinstance(exc, NotFound):

        response.data = {
            "success": False,
            "message": "Resource Not Found",
            "errors": response.data
        }

    else:

        response.data = {
            "success": False,
            "message": "Server Error",
            "errors": response.data
        }

    return response