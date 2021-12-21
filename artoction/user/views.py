from django.shortcuts import render , HttpResponse

# Create your views here.

def login_view(request , *args, **kwargs):
    return HttpResponse('hello from user')