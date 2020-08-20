from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def name(requests):
        return HttpResponse("I am N. Bhuvanesh Reddy, 1602-18-737-016")    

def index(response):
        return HttpResponse("<h1>This is the index of mycontacts,<br/> Search for mycontacts-..../whoami-.... </h1>")
