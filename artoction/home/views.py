from django.shortcuts import render, redirect


# Create your views here.

def landing_view(request, *args, **kwargs):
    return render(request,'home/index.html')

def productSearch(request, *args, **kwargs):
    if request.method == "GET":
        product_no = request.GET['id']
        return redirect(f"product/{product_no}")