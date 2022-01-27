# django imports 
from django.shortcuts import render , HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Account

    # django import for email and tokens
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage,send_mail


# app imports 
from .forms import RegistrationForm
    # token generater for mail 
from .tokens import generate_token

# python imports
import os


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
            return redirect('home')
        else:
            return render(request,'account/login.html')
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

        # passowrd verification and account creation with email to the user account
        if password1 == password2:
            myUser = Account.objects.create_user(email = email, username = username, password = password1)
            myUser.is_active = False
            myUser.save()
            # subject = "welcome"
            # message = "hello from the djanog app \n --with regards \n Avinash Kumar"
            # send_mail(subject, message, os.environ.get('EMAIL_ORIGIN'), [email])

            # activationg the account from the link sent to the email
            current_site = get_current_site(request)
            conf_email_subject = "Welcome to our site, please confirm your account"
            conf_message = render_to_string('account/conf_email.html',{
                'name' : myUser.username,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(myUser.pk)),
                'token' : generate_token.make_token(myUser),
            })

            conf_email = EmailMessage(
                conf_email_subject,
                conf_message,
                os.environ.get('EMAIL_ORIGIN'),
                [myUser.email],
            )
            conf_email.fail_silently = True
            conf_email.send()
            return redirect('home')
        else:
            return render(request, 'account/register.html',context)
            

    else:
        return render(request, 'account/register.html',context)




# activating the user account
def activate(request, uidb64, token ):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        my_user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        my_user = None
    if my_user is not None and generate_token.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
    return redirect('home')



def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('home')