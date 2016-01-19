from coreapi import Error
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, exceptions.ValidationError):
        error = Error(
            title='Invalid parameters.',
            content=exc.detail
        )
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    return exception_handler(exc, context)
