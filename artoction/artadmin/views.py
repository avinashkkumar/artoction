from django.shortcuts import render, redirect
from account.models import (
    Account,
    Address
)
from auction.models import Product
from home.models import Feedback

# Create your views here.

def adminHome(request, *args, **kwargs):
    context = {}
    return render(request,"admin/AdminHome.html",context)


def adminUpComingAuction(requset, *args, **kwargs):
    admin_upcoming_list = Product.objects.filter(isUpcoming=True)
    context = {
        'products' : admin_upcoming_list,
    }
    return render(requset,"admin/AdminUpComing.html",context)


def adminOngoingAuction(request, *args, **kwargs):
    admin_ongoing_list = Product.objects.filter(isOngoing=True)
    context = {
        'products' : admin_ongoing_list ,
    }
    return render(request,"admin/AdminOnGoing.html",context)


def adminCompletedAuction(request, *args, **kwargs):
    admin_completed_list = Product.objects.filter(isSold=True)
    context = {
        'products' : admin_completed_list ,
    }
    return render(request,"admin/AdminCompletedProduct.html",context)


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


def feedback_working(request, *args, **kwargs):
    feedback_list = Feedback.objects.all()
    context = {
        "feedbacks" : feedback_list,
    }
    return render(request,'admin/AdminWorkingFeedbackList.html',context)


def change_feedback_status(request, id, *args, **kwargs):
    if request.method == "POST":
        feedback = Feedback.objects.get(pk = id)
        feedback.status = request.POST.get("status")
        feedback.save()
        return redirect("feedbackWorking")


def admin_account_listing(request, *args, **kwargs):
    account_list = Account.objects.all()
    context = {
        "ulist" : account_list,
    }
    return render(request, "admin/AdminAccountListing.html",context)




def deactivate_account(request, id,*args, **kwargs):
    if request.user.is_admin:
        account = Account.objects.get(pk=id)
        account.is_active = False
        account.save()
        return redirect("userAccounts")
    else:
        return render(request, "account.something_went_wrong.html")




def activate_account(request, id,*args, **kwargs):
    if request.user.is_admin:
        account = Account.objects.get(pk=id)
        account.is_active = True
        account.save()
        return redirect("userAccounts")
    else:
        return render(request, "account.something_went_wrong.html")


def address_verification(request,*args, **kwargs):
    feedback_list = Address.objects.filter(is_verified=False,is_deneyed=False)
    context = {
        "plist" : feedback_list,
    }
    return render(request, "admin/AdminAddressVerification.html",context)