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
def editgroup(request, pk):
   edit = groupmodel(request.POST, request.FILES)

   # edit files
   editFiles = groupmodel.objects.get(id = pk)

   # store files
   files = uploadfilemodel.objects.all()

   if request.method == 'POST':
      editFiles.name = request.POST.get('name')
      editFiles.ideafile = request.POST.get('ideafile')
      editFiles.save()

      messages.info(request, "group updated")
      return redirect('/ideaNest')
  

   return render(request, 'editgroup.html', {'edit': edit, 'editFiles': editFiles, 'files': files})

def ungroup(request, pk):
   ungroup = groupmodel.objects.filter(id = pk)
   ungroup.delete()
   messages.info(request, 'files successfully ungrouped')

   return redirect('/ideaNest')

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

def groupfiles(request):
   # group file
   if request.method == "POST":
      groupfiles = groupmodel()
      groupfiles.ideafile = request.POST.get('forgroup')
      groupfiles.name = request.POST.get('groupname')
      groupfiles.save()

      messages.success(request, 'files grouped')

      return redirect('/ideaNest')
   
   return render(request, "ideaNest.html")

def ideaNest(request):
   
   # upload file
   if request.method == "POST":
      upload = uploadfilemodel()
      upload.name = request.POST.get('name')
      upload.description = request.POST.get('description')
 
      if len(request.FILES) != 0:
         upload.file = request.FILES['file']
         upload.cover = request.FILES['cover']

      upload.save()

      messages.success(request, 'idea file uploaded')

      return redirect('/ideaNest')

   # store files
   files = uploadfilemodel.objects.all()

   # fetch grouped files
   groupedfiles = groupmodel.objects.all()
        
   # # upload file
   # if request.method == 'POST':
   #      form = uploadfileform(request.POST, request.FILES)

   #      name = uploadfilemodel()
   #      name.name = request.POST.get('name')
   #      name.description = request.POST.get('description')

   #    #   for f in request.FILES.getlist('file'):
   #    #       print(str(f))

   #      # file handling
   #    #   handleUploadedFile(request.FILES['file'])
   #      modelInstance = form.save(commit=False)
   #      modelInstance.save()
   
   #    #   file = request.FILES.getlist('file')[0]
   #    #   fileModel = uploadfilemodel.objects.create(file = file)
   #    #   fileModel.save()
   #      messages.info(request, "idea file has been uploaded")
   #      # return HttpResponse("the name of uploaded file is " + str(fileModel.file))
   # else:
      #   form = uploadfileform()

   
   # return render(request, "ideaNest.html", {'form': form, 'files': files})
   return render(request, "ideaNest.html", {'files': files, 'groupedfiles': groupedfiles})

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

class ProjectDashboard(View):
   def get(self, request):
      try:
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id'])
         print(user)
         project = Project.objects.filter(user_id = user)
         context = {
            'user' : user,
            'project' : project
         }
         return render(request, "ProjectDashboard.html", context)
      except KeyError:
         return render(request, "ProjectDashboard.html")
   def post(self, request):
      if request.method == 'POST':
         projectID = request.POST.get('myID')
         form = Project(request.POST)
         user = request.session['id']
         ttle = request.POST.get('title')
         desc = request.POST.get('description')
         if 'btnProjCreate' in request.POST:
            form = Project(title = ttle, description = desc, user_id = user)
            form.save()
            return redirect('ProjectDashboard')
            # project = Project.objects.filter(user_id = user).latest('id') starts here
            # request.session['project_id'] = project.id
            # return redirect('ProjectDashboard') redirect to the newly created project
         elif 'btnProjDelete' in request.POST:
            Project.objects.get(id = projectID).delete()
         elif 'btnProjEdit' in request.POST:
            Project.objects.filter(id = projectID).update(title = ttle, description = desc, user_id = user)
      return redirect('ProjectDashboard')

def Relations(request):
   return render(request, "Relations.html")

## QUIZZZ
class CreateQuizView(View):
   def get(self,request):
      try:
         print("-------USER in SESSION-------")
         print(request.session['id'])
         user = User.objects.get(id = request.session['id']) 
         quiz = Quiz.objects.all()
        # user = User.objects.all()
         context ={
            'quiz' : quiz,
            'user' : user
         }

         return render(request, "CreateQuiz.html", context)
      except KeyError:
         return render(request, "CreateQuiz.html")
   def post(self, request):
      if request.method == 'POST':
         if 'btnCreate' in request.POST:
            form = Quiz(request.POST)
            user = request.session['id']
            name = request.POST.get('name')
            desc = request.POST.get('desc')
            date = request.POST.get('date')
            #print(user)
            form = Quiz( quiz_name = name, quiz_date = date,user_id = user, quiz_desc = desc)
            form.save()
            quiz = Quiz.objects.filter(user_id = user).latest('id')
            request.session['quiz_id'] = quiz.id
            return redirect('EditQuiz')
            #print(form.errors)
         elif 'btnEdit' in request.POST:
            q_id = request.POST.get('q_id')
            request.session['quiz_id'] = q_id
            return redirect('EditQuiz')
         elif 'btnDelete' in request.POST:
            quiz = request.POST.get('q_id')
            if quiz == request.session['quiz_id']:
               try:
                  del request.session['id'] #OR request.session.flush() to end session
               except KeyError:
                  pass
            else:
               Quiz.objects.get(id = quiz).delete()
               print('deleted successfully')
               return redirect('CreateQuiz')
         elif 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('About')
      return redirect('CreateQuiz')
  
class EditQuizView(View):
   def get(self,request):
      try:
         print("-------USER in SESSION-------")
         print(request.session['id'])
         print("-------Quiz in SESSION-------")
         print(request.session['quiz_id'])
         user = User.objects.get(id = request.session['id']) 
         #user = 
         quiz = Quiz.objects.get(id = request.session['quiz_id'])
         #question = Question.objects.all()
         question = Question.objects.filter(quiz_id = request.session['quiz_id']).order_by('-q_num')
         answer = Answer.objects.all()
        # user = User.objects.all()
         context ={
            'quiz' : quiz,
            'user' : user,
            'question' : question,
            'answer' : answer,
         }

         return render(request, "EditQuiz.html", context)
      except KeyError:
         return render(request, "EditQuiz.html")
   def post(self, request):
      if request.method == 'POST':
         if 'btnAddQuestion' in request.POST:
            form = Question(request.POST)
            quiz = request.session['quiz_id']
            num = request.POST.get('num')
            q = request.POST.get('ques')
            #print(user)
            form = Question( quiz_id = quiz, q_num = num ,question = q)
            form.save()
            #print(form.errors)
         #elif 'btnAddMe' in request.POST:
            #meid = request.POST.get('q_id')
         elif 'btnDelete' in request.POST:
            question = request.POST.get('q_id')
            print(question)
            Question.objects.get(id = question).delete()
            print('deleted successfully')
            return redirect('EditQuiz')
         elif 'btnAddAnswer' in request.POST:
            form = Answer(request.POST)
            option = request.POST.get('ans')
            q_id = request.POST.get('q_id')
            isAnswer = request.POST.get('isAnswer')
            if isAnswer == 'on':
               isAnswer = True
            else:
               isAnswer = False
            form = Answer( question_id = q_id, answer = option, isAnswer = isAnswer)
            form.save()
            #q_id = 
        # elif 'btnView' in request.POST:
         #    q_id = request.POST.get('q_id')
         #    request.session['quiz_id'] = q_id
         #   return redirect('ViewQuiz')
         elif 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('About')
      return redirect('EditQuiz')

def ViewQuiz(request):
   return render(request, "ViewQuiz.html")


class QuizView(View):
   def get(self,request):
      try:
         print("-------USER in SESSION-------")
         print(request.session['id'])
         print("-------Quiz in SESSION-------")
         print(request.session['quiz_id'])
         user = User.objects.get(id = request.session['id']) 
         quiz = Quiz.objects.get(id = request.session['quiz_id'])
         #question = Question.objects.all()
         question = Question.objects.filter(quiz_id = request.session['quiz_id']).order_by('-q_num')
         option = Answer.objects.all()
         answer = Answer.objects.filter(isAnswer = True)
        # user = User.objects.all()
         context ={
            'quiz' : quiz,
            'user' : user,
            'question' : question,
            'option' : option,
            'answer' : answer,
         }

         return render(request, "Quiz.html", context)
      except KeyError:
         return render(request, "Quiz.html")
   def post(self, request):
      return redirect('Quiz')


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

