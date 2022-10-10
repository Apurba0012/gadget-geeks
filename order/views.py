from django.shortcuts import render,HttpResponse

# Create your views here.
def return_view(request):
    return HttpResponse("<h1>This Is return Page</h1>")
def review_view(request):
    return HttpResponse("<h1>This Is review Page</h1>")