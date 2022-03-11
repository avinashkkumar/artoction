from django.shortcuts import render, redirect
from account.models import (
    Account,
    Address
)
from auction.models import Product
from home.models import Feedback

# Create your views here.

def adminHome(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        context = {}
        return render(request,"admin/AdminHome.html",context)
    else:
        return redirect("notFound")


def adminUpComingAuction(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        admin_upcoming_list = Product.objects.filter(isUpcoming=True)
        context = {
            'products' : admin_upcoming_list,
        }
        return render(request,"admin/AdminUpComing.html",context)
    else:
        return redirect("notFound")

def adminOngoingAuction(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        admin_ongoing_list = Product.objects.filter(isOngoing=True)
        context = {
            'products' : admin_ongoing_list ,
        }
        return render(request,"admin/AdminOnGoing.html",context)
    else:
        return redirect("notFound")

def adminCompletedAuction(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        admin_completed_list = Product.objects.filter(isSold=True)
        context = {
            'products' : admin_completed_list ,
        }
        return render(request,"admin/AdminCompletedProduct.html",context)
    else:
        return redirect("notFound")

def cycle(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
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
    else:
        return redirect("notFound")

def feedback_working(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        feedback_list = Feedback.objects.all()
        context = {
            "feedbacks" : feedback_list,
        }
        return render(request,'admin/AdminWorkingFeedbackList.html',context)
    else:
        return redirect("notFound")

def change_feedback_status(request, id, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "POST":
            feedback = Feedback.objects.get(pk = id)
            feedback.status = request.POST.get("status")
            feedback.save()
            return redirect("feedbackWorking")
    else:
        return redirect("notFound")

def admin_account_listing(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        account_list = Account.objects.all()
        context = {
            "ulist" : account_list,
        }
        return render(request, "admin/AdminAccountListing.html",context)
    else:
        return redirect("notFound")



def deactivate_account(request, id,*args, **kwargs):
    if request.user.is_admin:
        account = Account.objects.get(pk=id)
        account.is_active = False
        account.save()
        return redirect("userAccounts")
    else:
        return render(request, "account.something_went_wrong.html")




def activate_account(request, id,*args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        if request.user.is_admin:
            account = Account.objects.get(pk=id)
            account.is_active = True
            account.save()
            return redirect("userAccounts")
        else:
            return redirect("notFound")
    else:
            return redirect("notFound")


def address_verification(request,*args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        feedback_list = Address.objects.filter(is_verified=False,is_deneyed=False)
        context = {
            "plist" : feedback_list,
        }
        return render(request, "admin/AdminAddressVerification.html",context)
    else:
            return redirect("notFound")




def change_address_status(request, id, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        if request.method == "POST":
            address = Address.objects.get(pk = id)
            if request.POST.get("status") == "apparove":
                address.is_verified = True
                account = address.user
                account.verified_address = True
                account.save()
            elif request.POST.get("status") == "reject":
                address.is_deneyed = True
            address.save()
        return redirect("addressVerification")
    else:
            return redirect("notFound")


def remove_product(request, id, *args, **kwargs):
    if request.user.is_authenticated and request.user.is_admin:
        product = Product.objects.filter(pk = id)
        product.delete()
        return redirect(request.headers.get("Referer"))
    else:
        return redirect("notFound")