from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel


def example_response(request):
    MyModel.objects.create(
        name='Bob',
        created=True
    )
    return HttpResponse("OK")
