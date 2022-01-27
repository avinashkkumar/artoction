"""artoction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include 
from django.conf import settings
from django.conf.urls.static import static
from artoction.settings import MEDIA_ROOT

from home.views import (
    landing_view,
    )

from auction.views import (
    auction_land,
    ongoing,
    upcoming,
    completed,
    product,
)

from account.views import (
    account,
    login_view,
    logout_view, 
    register_view,
    activate,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing_view, name="home"),
    path('auction', auction_land, name='auctions'),
    path('ongoing', ongoing, name="ongoing"),
    path('upcoming',upcoming , name="upcoming"),
    path('completed', completed, name="completed"),
    path('account', account, name="account"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('register', register_view, name="register"),
    path('product/<int:id>', product, name="product"),
    path('activate/<uidb64>/<token>', activate , name="activate" )



]

urlpatterns += static(settings.MEDIA_URL, document_root = MEDIA_ROOT) 