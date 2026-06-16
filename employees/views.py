from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "employees/index.html")
def home(request):
    return render(request, "employees/home.html")
def about(request):
    return render(request, "employees/about.html")
def contact(request):
    return render(request, "employees/contact.html")