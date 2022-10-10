from django.shortcuts import render,HttpResponse

# Create your views here.
def chat_view(request):
    return HttpResponse("<h1>This Is chat Page</h1>")
def cancelOrder_view(request):
    return HttpResponse("<h1>This Is cancel order Page</h1>")
def trackOrder_view(request):
    return HttpResponse("<h1>This Is track order Page</h1>")
def editAccount_view(request):
    return HttpResponse("<h1>This Is edit account Page</h1>")
def resetPassword_view(request):
    return HttpResponse("<h1>This Is reset password Page</h1>")
