from django.shortcuts import render

# Create your views here.
from utils import restful


def banner(request):
    data = ''
    return restful.ok(data=data)