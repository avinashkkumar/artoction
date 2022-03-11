from django.shortcuts import render, redirect
from account.models import Account
from home.models import Feedback

# Create your views here.

def landing_view(request, *args, **kwargs):
    return render(request,'home/index.html')

def productSearch(request, *args, **kwargs):
    if request.method == "GET":
        product_no = request.GET['id']
        return redirect(f"product/{product_no}")

def feedback(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            account = Account.objects.get(email=request.POST['email'])
        except:
            account = None
        if account is not None:
            review = Feedback()
            review.user = account
            review.feedback = request.POST['fetext']
            review.save()
        last = request.POST['next']
        return redirect(last)


def page_not_found(request, *args, **kwargs):
    return render(request,"pageNotFound.html")


def how_it_works(request, *args, **kwargs):
    return render(request, "page.html")