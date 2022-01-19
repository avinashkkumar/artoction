# django imports 
from django.shortcuts import render , HttpResponse, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth import get_user_model
from .models import Account


# app imports 
from .forms import RegistrationForm


# Create your views here.
# Account = get_user_model()

# account view here
def account(request, *args, **kwargs):
    context = {'proName' : 'Avinash Kumar',
               'prodNo': 5,
               'title': 'Product Title',
               'receviedUserName' : 'Chiptole',
               'productCategory' : 'Digital Art',
               'soldPrice': 1279 
                }
    return render(request, "account/account.html",context)



# login page here
def login_view(request, *args, **kwargs):
    if (request.method == 'POST'):
        user = request.POST.get('username')
        pas  = request.POST.get('password1')
        user = authenticate(request,username=user,password=pas)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('upcoming')
        else:
            print(user)
            return redirect('login')
    else:
        return render(request, 'account/login.html')



# register page here

def register_view(request, *args, **kwargs):
    context = {}
    # form = RegistrationForm() 
    # I am not using the forms and directly saving the forms from here itself
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    elif (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            myUser = Account.objects.create_user(email = email, username = username, password = password1)
            myUser.save()
        else:
            return render(request, 'account/register.html',context)
            

    else:
        form = RegistrationForm()
        context['form'] = form
    return render(request, 'account/register.html',context)