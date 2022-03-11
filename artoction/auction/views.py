from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from auction.models import Product
from account.models import Account
import random

# Create your views here.

# auction listing page is here 
def auction_land(request, *args, **kwargs):
    three_ongoing_count     = Product.objects.filter(isOngoing=True).count()
    three_ongoing_count     = three_ongoing_count - 3
    Ongoing_rand_start      = random.randint(0,three_ongoing_count)
    ongoing_rand_end        = Ongoing_rand_start + 3
    three_ongoing           = Product.objects.filter(isOngoing=True)[Ongoing_rand_start:ongoing_rand_end]

    three_upcoming_count    = Product.objects.filter(isUpcoming=True).count()
    three_upcoming_count    = three_upcoming_count - 3
    upcoming_rand_start     = random.randint(0, three_upcoming_count)
    upcoming_rand_end       = upcoming_rand_start + 3
    three_upcoming          = Product.objects.filter(isUpcoming=True)[upcoming_rand_start:upcoming_rand_end]

    completed_count         = Product.objects.filter(isSold=True).count()
    completed_count         = completed_count - 3
    rand_start              = random.randint(0, completed_count)
    rnad_end                = rand_start + 3
    three_completed         = Product.objects.filter(isSold=True)[rand_start:rnad_end]
    context = {
        'upcomings' : three_upcoming,
        'ongoings' : three_ongoing,
        'completed' : three_completed,
}
    return render(request,"auction/auctionListing.html",context)



# ongoing auctions page is here
def ongoing(request, *args, **kwargs):
    ongoing_product_list = Product.objects.filter(isOngoing=True)
    print(ongoing_product_list)
    context = {
        'ongoing':ongoing_product_list,
    }
    return render(request,"auction/ongoingAuction.html",context)




# upcoming auction page is here 
def upcoming(request, *args, **kwargs):
    upcoming_product_list = Product.objects.filter(isUpcoming=True)
    context = {
        'upcoming' : upcoming_product_list,
    }
    return render(request,"auction/upcomingAuctions.html",context)




# completed auction page is here 
def completed(request, *args, **kwargs):
    completed_product_list = Product.objects.filter(isSold=True)
    context = {
        'completed': completed_product_list,}
    return render(request,"auction/completedAuction.html",context)


# product view here 
def product(request,id = None, *args, **kwargs):
    product_obj = Product.objects.get(id=id)
    context = {'this':product_obj}
    return render(request, 'auction/productView.html',context)


def productCreate(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['Title']
            description = request.POST['description']
            basePrice = request.POST['basePrice']
            # getting first image
            try:
                image1 = request.FILES['image1']
            except:
                image1 = None
            # getting second image
            try:
                image2 = request.FILES['image2']
            except:
                image2 = None
            # getting third image
            try:
                image3 = request.FILES['image3']
            except:
                image3 = None
            # getting fourth image
            try:
                image4 = request.FILES['image4']
            except:
                image4 = None
            # getting fifth image    
            try:
                image5 = request.FILES['image5']
            except:
                image5 = None

            listed_by_user                  = Account.objects.get(id=request.user.pk)
            current_product                 = Product()
            current_product.name            = title
            current_product.description     = description
            current_product.base_price      = basePrice 
            current_product.current_price   = basePrice
            current_product.listedBy        = listed_by_user
            current_product.category        = None
            current_product.image1          = image1
            current_product.image2          = image2
            current_product.image3          = image3
            current_product.image4          = image4
            current_product.image5          = image5
            current_product.isUpcoming      = True
            current_product.save()
            context = {
                "output" : "Your product has been added to the upcoming auction listing",
                "url" : "/",
                "buttonName" : "Get back Home",
                "symbol" : "✅"
            }
            return render(request,'sucessPage.html',context)
        elif request.method == "GET":
            return render(request, 'auction/addProduct.html')
    else:
        return redirect("login")


def price_update(request, id, *args, **kwargs):
    if request.method == "POST":
        product = Product.objects.get(pk = id)
        if int(product.current_price) < int(request.POST['bid']):
            product.current_price = request.POST['bid']
            product.current_bidder = request.user.username
            product.save()
        else:
            context = {
                "output" : "Your Price was not updated",
                "url" : request.headers.get("Referer"),
                "buttonName" : "Get Back",
                "symbol" : "❌"
            }
            return render(request,"sucessPage.html",context)
        return redirect('product',id)