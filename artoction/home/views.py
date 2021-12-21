from django.shortcuts import render


# Create your views here.

def landing_view(request, *args, **kwargs):
    
    a = "hello"
    context = {'info' : a}
    return render(request,'home/index.html',context)