"""gadgetGeeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
import home.views
import product.views

import order.views
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', home.views.home_view,name='home'),
    path('products/', home.views.products_view,name='products'),
    path('product-details/', home.views.product_details_view,name='productDetails'),
    path('cart/', home.views.cart_view,name='cart'),
    path('checkout/', home.views.checkout_view,name='checkout'),
    path('my-account/', home.views.my_account_view,name='myAcc'),
    path('wishlist/', home.views.wishlist_view,name='wishlist'),
    path('login-register/', home.views.login_and_register_view,name='loginRegister'),
    path('contact-us/', home.views.contact_us_view,name='contact'),

]
