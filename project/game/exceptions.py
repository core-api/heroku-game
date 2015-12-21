from coreapi import Error
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    if isinstance(exc, exceptions.ValidationError):
        messages = []
        for key, value in exc.detail.items():
            if key == 'non_field_errors':
                messages.extend(value)
            else:
                for item in value:
                    messages.append('%s - %s' % (key, item))
        error = Error(messages)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    return exception_handler(exc, context)
