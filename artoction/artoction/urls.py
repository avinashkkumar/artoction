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

from artadmin.views import (
    adminHome,
    adminUpComingAuction,
    adminOngoingAuction,
    adminCompletedAuction,
    cycle,
    feedback_working,
    admin_account_listing,
    deactivate_account,
    activate_account,
    change_feedback_status,
    address_verification,
    change_address_status,
    remove_product,
)


from home.views import (
    landing_view,
    productSearch,
    feedback,
    page_not_found,
    how_it_works,
    )

from auction.views import (
    auction_land,
    ongoing,
    upcoming,
    completed,
    product,
    productCreate,
    price_update,
)

from account.views import (
    account,
    login_view,
    logout_view, 
    register_view,
    activate,
    forgot_password,
    password_reset_view,
    change_address_view,
    Change_password,
)

urlpatterns = [
    # django database admin 
    path('admin/', admin.site.urls),

    # admin app
    path('artadmin/', adminHome, name="adminHome"),
    path('adminupcoming/', adminUpComingAuction, name="adminUpcoming"),
    path('adminongoing/', adminOngoingAuction, name="adminOngoing"),
    path('admincompleted/', adminCompletedAuction, name="adminCompleted"),
    path('cycle/', cycle, name="cycle"),
    path('feedback-list',feedback_working,name="feedbackWorking"),
    path('user-list',admin_account_listing,name="userAccounts"),
    path('activate-user/<int:id>',activate_account,name="activateUser"),
    path('deactivate-user/<int:id>',deactivate_account,name="deactivateUser"),
    path('feedback-status-change/<int:id>',change_feedback_status,name="changeFeedbackStatus"),
    path('address-verification',address_verification,name="addressVerification"),
    path('<int:id>/address-status',change_address_status,name='addressStatus'),
    path("<int:id>/remove-product",remove_product,name="removeProduct"),

    # home app
    path('', landing_view, name="home"),
    path('search', productSearch, name="search"),
    path('feedback', feedback, name='feedback'),
    path('page-not-found',page_not_found,name='notFound'),
    path('how-it-works',how_it_works,name="howItWorks"),

    # auction app
    path('auction', auction_land, name='auctions'),
    path('ongoing', ongoing, name="ongoing"),
    path('upcoming', upcoming , name="upcoming"),
    path('completed', completed, name="completed"),
    path('create', productCreate, name="create"),
    path('product/<int:id>', product, name="product"),
    path('price-update/<int:id>', price_update, name="priceUpdate"),

    # account app
    path('account/<int:id>', account, name="account"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('register', register_view, name="register"),
    path('forgot-password', forgot_password , name="forgotPassword"),
    path('activate/<uidb64>/<token>', activate , name="activate"),
    path('<uidb64>/<token>/set-password/', password_reset_view, name="resetPassword"),
    path('address-change/<int:id>', change_address_view,name='addressChange'),
    path('change-password',Change_password,name='changePassword'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = MEDIA_ROOT) 