from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LandingPage(request):
   return render(request, "LandingPage.html")

def About(request):
   return render(request, "About.html")

def Signin(request):
   return render(request, "Signin.html")

def LM_CreateChapter(request):
   return render(request, "LM_CreateChapter.html")