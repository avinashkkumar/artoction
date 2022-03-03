from django.shortcuts import render, redirect
from account.models import Account
from auction.models import Product

# Create your views here.

def adminHome(request, *args, **kwargs):
    context = {}
    return render(request,"admin/AdminHome.html",context)


def adminUpComingAuction(requset, *args, **kwargs):
    context = {}
    return render(requset,"admin/AdminUpComing.html",context)


def adminOngoingAuction(request, *args, **kwargs):
    context = {}
    return render(request,"admin/AdminOnGoing.html",context)


def adminCompletedAuction(request, *args, **kwargs):
    context = {}
    return render(request,"admin/AdminCompletedProduct.html")


def cycle(request, *args, **kwargs):
    ongoing_product_list = Product.objects.filter(isOngoing=True)
    for y in ongoing_product_list:
        y.isOngoing = False
        y.isSold = True
        y.save()
    
    upcoming_product_list = Product.objects.filter(isUpcoming=True)
    for x in upcoming_product_list:
        x.isUpcoming = False
        x.isOngoing = True
        x.save()
    return redirect('adminHome')