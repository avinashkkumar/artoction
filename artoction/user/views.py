from django.shortcuts import render , HttpResponse

# Create your views here.

# account view here
def account(request, *args, **kwargs):
    context = {'proName' : 'Avinash Kumar',
               'prodNo': 5,
               'title': 'Product Title',
               'receviedUserName' : 'Chiptole',
               'productCategory' : 'Digital Art',
               'soldPrice': 1279 
                }
    return render(request, "user/account.html",context)



# login page here
def login(request, *args, **kwargs):
    return render(request, 'user/login.html')



# register page here
def register(request, *args, **kwargs):
    return render(request, 'user/register.html')