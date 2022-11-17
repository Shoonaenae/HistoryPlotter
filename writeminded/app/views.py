from app.forms import uploadfileform
from .models import uploadfilemodel
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# import pyrebase

# config = {
#    "apiKey": "AIzaSyB2oD3Lc-TNvzUuzaYHnKTwIrtNgDqHq10",
#    "authDomain": "software-engineering-2-776a7.firebaseapp.com",
#    "projectId": "software-engineering-2-776a7",
#    "storageBucket": "software-engineering-2-776a7.appspot.com",
#    "messagingSenderId": "879870492169",
#    "appId": "1:879870492169:web:d61f61d709413cd447c2d8",
#    "measurementId": "G-MQSZBBXVRC"
# }

# # firebase authentication
# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()

# Create your views here.
def LandingPage(request):
   return render(request, "LandingPage.html")

def ideaNest(request):
   if request.method == 'POST':
        form = uploadfileform(request.POST, request.FILES)

        for f in request.FILES.getlist('file'):
            print(str(f))

        file = request.FILES.getlist('file')[0]
        fileModel = uploadfilemodel.objects.create(file = file)
        fileModel.save()
        messages.info(request, "file has been uploaded")
        # return HttpResponse("the name of uploaded file is " + str(fileModel.file))
   else:
        form = uploadfileform()
    
   return render(request, "ideaNest.html", {'form': form})

def About(request):
   return render(request, "About.html")

def Signin(request):
   return render(request, "Signin.html")

def Signup(request):
   return render(request, "Signup.html")

def LM_CreateChapter(request):
   return render(request, "LM_CreateChapter.html")

def ProjectDashboard(request):
   return render(request, "ProjectDashboard.html")

def Relations(request):
   return render(request, "Relations.html")

def CreateQuiz(request):
   return render(request, "CreateQuiz.html")

def EditQuiz(request):
   return render(request, "EditQuiz.html")

def ViewQuiz(request):
   return render(request, "ViewQuiz.html")