from app.functions import handleUploadedFile
from app.forms import uploadfileform
from .models import uploadfilemodel
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LandingPage(request):
   return render(request, "LandingPage.html")

def ideaNest(request):
   if request.method == 'POST':
        form = uploadfileform(request.POST, request.FILES)

      #   for f in request.FILES.getlist('file'):
      #       print(str(f))

        # file handling
        handleUploadedFile(request.FILES['file'])
        modelInstance = form.save(commit=False)
        modelInstance.save()

      #   file = request.FILES.getlist('file')[0]
      #   fileModel = uploadfilemodel.objects.create(file = file)
      #   fileModel.save()
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