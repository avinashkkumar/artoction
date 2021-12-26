from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

# auction listing page is here 
def auction_land(request, *args, **kwargs):
    context = {'title':"This is a title" ,
               'price':1999 ,
               'buyer':"Buyer name"}
    return render(request,"auction/auctionListing.html",context)



# ongoing auctions page is here
def ongoing(request, *args, **kwargs):
    context = {'title':"This is a title" ,
               'price':1999 ,
               'buyer':"Buyer name"}
    return render(request,"auction/ongoingAuction.html",context)




# upcoming auction page is here 
def upcoming(request, *args, **kwargs):
    context = {'titleHead':'Upcoming Auctions',
               'title':"Product Name" ,
               'price':1999 ,
               'buyer':"Buyer name"}
    return render(request,"auction/upcomingAuctions.html",context)




# completed auction page is here 
def completed(request, *args, **kwargs):
    
    context = {'titleHead':'Completed Auctions',
               'title':"Product Name" ,
               'price':1999 ,
               'buyer':"Buyer name"}
    return render(request,"auction/completedAuction.html",context)


# product view here 
def product(request, *args, **kwargs):
    context = {"title":"Product Title is Title",
               "Price" : 6541,
               "prodUser":"User Name",
               "notes":"This is a note from the auther of the post"}
    return render(request, 'auction/productView.html',context)