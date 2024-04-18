from django.shortcuts import render
from django.http import HttpResponse

def notifications_page(request):
    return HttpResponse('Hello World!')