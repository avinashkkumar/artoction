from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from auction.models import Product
from account.models import Account

# Create your views here.

# auction listing page is here 
def auction_land(request, *args, **kwargs):
    three_ongoing = Product.objects.filter(isOngoing=True)[:3]
    three_upcoming = Product.objects.filter(isUpcoming=True)[:3]
    three_completed = Product.objects.filter(isSold=True)[:3]
    context = {
        'upcomings' : three_upcoming,
        'ongoings' : three_ongoing,
        'completed' : three_completed,
}
    return render(request,"auction/auctionListing.html",context)



# ongoing auctions page is here
def ongoing(request, *args, **kwargs):
    ongoing_product_list = Product.objects.filter(isOngoing=True)
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
        'completed': completed_product_list,
        'titleHead':'Completed Auctions',
               'title':"Product Name" ,
               'price':1999 ,
               'buyer':"Buyer name"}
    return render(request,"auction/completedAuction.html",context)


# product view here 
def product(request,id = None, *args, **kwargs):
    product_obj = Product.objects.get(id=id)
    context = {'this':product_obj}
    return render(request, 'auction/productView.html',context)


def productCreate(request, *args, **kwargs):
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

        listed_by_user = Account.objects.get(id=request.user.pk)
        current_product = Product()
        current_product.name = title
        current_product.description = description
        current_product.base_price = basePrice 
        current_product.current_price = basePrice
        current_product.listedBy = listed_by_user
        current_product.category = None
        current_product.image1 = image1
        current_product.image2 = image2
        current_product.image3 = image3
        current_product.image4 = image4
        current_product.image5 = image5
        current_product.isUpcoming = True
        current_product.save()
    context = {}
    return render(request, 'auction/addProduct.html',context)



