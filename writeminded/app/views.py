from django.views import View
from app.functions import handleUploadedFile
from app.forms import uploadfileform
from .models import User, uploadfilemodel
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def LandingPage(request):
   return render(request, "LandingPage.html")

def ideaNest(request):

   # store files
   files = uploadfilemodel.objects.all()

   # upload file
   if request.method == 'POST':
        form = uploadfileform(request.POST, request.FILES)
        
        name = uploadfilemodel()
        name.name = request.POST.get('name')
        name.name = request.POST.get('description')

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
   
   return render(request, "ideaNest.html", {'form': form, 'files': files})

def About(request):
   return render(request, "About.html")

class SigninView(View):
   def get(self, request):
      return render(request, "Signin.html")
   def post(self, request):
      user = request.POST.get("user_email") # get user or email
      passw = request.POST.get("pass")
      if User.objects.filter(username = user).exists():
         meuser = User.objects.get(username = user) # get the object
         if meuser.password == passw:
            request.session['id'] = meuser.id # log in user
            print('login')
            return redirect('About')
         else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')
      elif User.objects.filter(email_address = user).exists():
         meuser = User.objects.get(email_address = user) # get the object
         if meuser.password == passw:
            request.session['id'] - meuser.id # log in user
            return redirect('About')
         else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')
      else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')


class SignupView(View):
   def get(self,request):
      return render(request, "Signup.html")
   def post(self,request):
      if request.method == "POST":
         form = User(request.POST)
         user = request.POST.get("username")
         passw = request.POST.get("password")
         confirm = request.POST.get("confirm")
         email = request.POST.get("email")
         fname = request.POST.get("fname")
         lname = request.POST.get("lname")
         if passw == confirm:
            form = User(username = user, password = passw, email_address = email, first_name = fname, last_name = lname)
            form.save()
            return redirect('Signin')
         else:
            print(form.errors)
            return redirect('Signup')

         

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