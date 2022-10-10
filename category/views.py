from django.shortcuts import render,HttpResponse

# Create your views here.
def product_view(request):
    return HttpResponse("<h1>This Is product Page</h1>")
def buy_view(request):
    return HttpResponse("<h1>This Is buy Page</h1>")
def payment_view(request):
    return HttpResponse("<h1>This Is payment Page</h1>")