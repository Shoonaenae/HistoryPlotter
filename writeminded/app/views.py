import os

from django.views import View
from app.functions import handleUploadedFile
from app.forms import uploadfileform
from .models import *
from django.contrib import messages
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Materials
from .forms import DescriptionForm

# Create your views here.
def ideanestdelete(request, pk):
   file = uploadfilemodel.objects.filter(id = pk)
   file.delete()
   messages.info(request, 'file has been deleted')
   return redirect('/ideaNest')

def ideaNestEdit(request, pk):
   edit = uploadfileform(request.POST, request.FILES)

   # edit files
   editFiles = uploadfilemodel.objects.get(id = pk)

   if request.method == 'POST':
      if len(request.FILES) != 0: # if there is a file
         if len(editFiles.file) > 0: # remove file
            os.remove(editFiles.file.path)
         
         editFiles.file = request.FILES['file']
      editFiles.name = request.POST.get('name')
      editFiles.description = request.POST.get('description')
      editFiles.save()

      messages.info(request, "idea file has been updated")
      return redirect('/ideaNest')

   return render(request, 'editIdeaNest.html', {'edit': edit, 'editFiles': editFiles})

def ideaNest(request):
   
   # store files
   files = uploadfilemodel.objects.all()

   # upload file
   if request.method == 'POST':
        form = uploadfileform(request.POST, request.FILES)
        
        name = uploadfilemodel()
        name.name = request.POST.get('name')
        name.description = request.POST.get('description')

      #   for f in request.FILES.getlist('file'):
      #       print(str(f))

        # file handling
        handleUploadedFile(request.FILES['file'])
        modelInstance = form.save(commit=False)
        modelInstance.save()

      #   file = request.FILES.getlist('file')[0]
      #   fileModel = uploadfilemodel.objects.create(file = file)
      #   fileModel.save()
        messages.info(request, "idea file has been uploaded")
        # return HttpResponse("the name of uploaded file is " + str(fileModel.file))
   else:
        form = uploadfileform()
   
   return render(request, "ideaNest.html", {'form': form, 'files': files})

def LandingPage(request):
   return render(request, "LandingPage.html")

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
            print('login!')
            print(meuser.username)
            return redirect('About')
         else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')
      elif User.objects.filter(email_address = user).exists():
         meuser = User.objects.get(email_address = user) # get the object
         if meuser.password == passw:
            request.session['id'] = meuser.id # log in user
            return redirect('About')
            print('login!')
            print(meuser.username)
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

## QUIZZZ
class CreateQuizView(View):
   def get(self,request):
      print("-------USER in SESSION-------")
      print(request.session['id'])
      #user = 
      quiz = Quiz.objects.all()
      user = User.objects.all()
      context ={
         'quiz' : quiz,
         'user' : user
      }

      return render(request, "CreateQuiz.html", context)
   def post(self, request):
      if request.method == 'POST':
         #if 'btnCreate' in request.POST:
            form = Quiz(request.POST)
            user = request.session['id']
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            date = request.POST.get('date')
            #print(user)
            form = Quiz( quiz_name = name, quiz_date = date,user_id = user, quiz_desc = desc)
            form.save()
            #print(form.errors)
      return redirect('CreateQuiz')
  

def EditQuiz(request):
   return render(request, "EditQuiz.html")

def ViewQuiz(request):
   return render(request, "ViewQuiz.html")

def QuizView(request):
   return render(request, "Quiz.html")

class MaterialsView(ListView):
    model = Materials 
    template_name = 'LM_materials.html'

class MaterialDetailView(DetailView):
    model = Materials
    template_name= 'LM_material_details.html'
    context_object_name = 'mat'

class AddMaterialsView(CreateView):
    model = Materials
    form_class = DescriptionForm
    template_name = 'LM_add_materials.html'
    #fields = '__all__'

class UpdateMaterialDescriptionsView(UpdateView):
    model = Materials
    template_name = 'LM_edit_materialdescriptions.html'
    fields = ['title', 'description']