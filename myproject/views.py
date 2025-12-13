"""
Views for myproject.
"""
from django.http import HttpResponse


def index(request):
    """
    Returns a simple Hello World message.
    """
    return HttpResponse("Hello World")


def placeholder(request):
    """
    Returns a placeholder string that can be replaced later.
    """
    return HttpResponse("<<<py-place-holder>>>")
