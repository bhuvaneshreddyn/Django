from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
        return HttpResponse("<h1>Welcome!!</h1>")

def home(request):
        return HttpResponse("<h1>Welcome to Home Page!</h1>")

def aboutus(response):
        return HttpResponse("Name: N. Bhuvanesh Reddy<hr>Roll Number: 1602-18-737-016")

def myhobbies(response):
        return HttpResponse("Hobbies: Cycling, Badminton, Watching anime")
