from django.shortcuts import render

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