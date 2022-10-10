from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'home.html')
def products_view(request):
    return render(request, 'products.html')
def product_details_view(request):
    return render(request, 'product_details.html')
def cart_view(request):
    return render(request, 'cart.html')
def checkout_view(request):
    return render(request, 'checkout.html')
def my_account_view(request):
    return render(request, 'my_account.html')
def wishlist_view(request):
    return render(request, 'wishlist.html')
def login_and_register_view(request):
    return render(request, 'login_and_register.html')
def contact_us_view(request):
    return render(request, 'contact_us.html')
