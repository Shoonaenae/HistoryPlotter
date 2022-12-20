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
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Materials
from .forms import DescriptionForm, EditForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator

# Create your views here.

class editgroup(View):
   def get(self,request, pk):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id']) 
         # edit files
         editFiles = groupmodel.objects.get(id = pk)
         files = uploadfilemodel.objects.all()
         
         return render(request, 'editgroup.html', {'editFiles': editFiles, 'user' : user, 'files': files})
      except KeyError: 
         # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
   
   def post(self, request, pk):
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

class ideaNestEdit(View):
   def get(self,request, pk):
       try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id']) 
         # edit files
         editFiles = uploadfilemodel.objects.get(id = pk)
         
         return render(request, 'editIdeaNest.html', {'editFiles': editFiles, 'user' : user})
       except KeyError: 
         # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")

   def post(self, request, pk):

      # edit files
      editFiles = uploadfilemodel.objects.get(id = pk)

      if request.method == 'POST':
         if len(request.FILES) != 0: # if there is a file
            if len(editFiles.file) > 0: # remove file
               os.remove(editFiles.file.path)
            
            editFiles.file = request.FILES['file']
            
            if len(editFiles.cover) > 0: # remove file
               os.remove(editFiles.cover.path)
            
            editFiles.cover = request.FILES['cover']
         editFiles.name = request.POST.get('name')
         editFiles.description = request.POST.get('description')
         editFiles.save()

         messages.info(request, "idea file has been updated")
         return redirect('/ideaNest')

class groupfiles(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         projectID = request.session['proj_id']
         user = User.objects.get(id = request.session['id']) 

         groupedfiles = groupmodel.objects.filter(user_id = user, project_id = projectID)

        # user = User.objects.all()
         context ={
            'user' : user,
            'groupedfiles': groupedfiles
         }

         return render(request, "ideaNest.html", context)
      except KeyError: 
         # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")

   def post(self,request):
      # group file
      if request.method == "POST":
         groupfiles = groupmodel()
         groupfiles.project_id = request.session['proj_id']
         groupfiles.user_id = request.session['id']
         groupfiles.ideafile = request.POST.get('forgroup')
         groupfiles.name = request.POST.get('groupname')
         groupfiles.save()

         messages.success(request, 'files grouped')

         return redirect('/ideaNest')
      
      return render(request, "ideaNest.html")

class ideaNest(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         projectID = request.session['proj_id']
         user = User.objects.get(id = request.session['id']) 

         # store files
         files = uploadfilemodel.objects.filter(user_id = user, project_id = projectID)
         groupedfiles = groupmodel.objects.filter(user_id = user, project_id = projectID)

        # user = User.objects.all()
         context ={
            'user' : user,
            'files': files,
            'groupedfiles': groupedfiles
         }

         return render(request, "ideaNest.html", context)
      except KeyError: 
         # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")

   def post(self,request):
      if request.method == 'POST':

        # upload file
         upload = uploadfilemodel()

         upload.projectid = request.session['proj_id']
         upload.user_id = request.session['id']
         upload.name = request.POST.get('name')
         upload.description = request.POST.get('description')
         upload.project_id = request.session['proj_id']
         if len(request.FILES) != 0:
            upload.file = request.FILES['file']
            upload.cover = request.FILES['cover']
            upload.save()
            
         if 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('LandingPage')

         messages.success(request, 'idea file uploaded')

      return redirect('/ideaNest')

class LandingPageView(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id']) 
        # user = User.objects.all()
         context ={
            'user' : user
         }
         return render(request, "LandingPage.html", context)
      except KeyError: 
         return render(request, "LandingPage.html")
   def post(self,request):
      if request.method == 'POST':
         if 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('LandingPage')

class AboutView(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id']) 
        # user = User.objects.all()
         context ={
            'user' : user
         }
         return render(request, "About.html", context)
      except KeyError: 
         #messages.error(request, 'You must login before you can access this function')
         return render(request, "About.html")
   def post(self,request):
      if request.method == 'POST':
         if 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('LandingPage')

# @csrf_exempt
@method_decorator(csrf_protect,name='post')
class SigninView(View):
   def get(self, request):
      return render(request, "Signin.html")
   # @csrf_protect
   def post(self, request):
      user = request.POST.get("user_email") # get user or email
      passw = request.POST.get("pass")
      if User.objects.filter(username = user).exists():
         meuser = User.objects.get(username = user) # get the object
         if meuser.password == passw:
            request.session['id'] = meuser.id # log in user
            print('login!')
            print(meuser.username)
            return redirect('LandingPage')
         else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')
      elif User.objects.filter(email_address = user).exists():
         meuser = User.objects.get(email_address = user) # get the object
         if meuser.password == passw:
            request.session['id'] = meuser.id # log in user
            return redirect('LandingPage')
         else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')
      else:
            messages.error(request, 'Username/Email or Password is incorrect')
            return redirect('Signin')


# @csrf_exempt
@method_decorator(csrf_protect,name='post')
class SignupView(View):
   def get(self,request):
      return render(request, "Signup.html")
   # @csrf_protect
   def post(self,request):
      if request.method == "POST":
         form = User(request.POST)
         print(request.COOKIES('csrftoken'))
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

## PROJECT
class ProjectDashboard(View):
   def get(self, request):
      try:
         user = User.objects.get(id = request.session['id'])
         print("-------USER in SESSION-------")
         print(user)
         project = Project.objects.filter(user_id = user)
         context = {
            'user' : user,
            'project' : project
         }
         return render(request, "ProjectDashboard.html", context)
      except KeyError:
          # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
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
         elif 'viewProj' in request.POST:
            request.session['proj_id'] = projectID
            return redirect('ProjectView')
         elif 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('LandingPage')
      return redirect('ProjectDashboard')

class ProjectView(View):
   def get(self, request):
      try:
         user = User.objects.get(id = request.session['id'])
         print("-------USER in SESSION-------")
         print(user)
         projectID = request.session['proj_id']
         project = Project.objects.filter(user_id = user, id = projectID)
         context = {
            'user' : user,
            'project' : project
         }
         return render(request, "ProjectView.html", context)
      except KeyError:
          # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
   def post(self,request):
      if request.method == 'POST':
         if 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('LandingPage')

## RELATIONS
class Relation(View):
   def get(self, request):
      try:
         user = User.objects.get(id = request.session['id'])
         print("-------USER in SESSION-------")
         print(user)
         projectID = request.session['proj_id']
         project = Project.objects.filter(user_id = user, id = projectID)
         print("RELATIONS")
         print("PROJECT ID: ", projectID)
         relations = Relations.objects.filter(user_id = user, project_id = projectID)
         materials = Materials.objects.filter(author = user, project_id = projectID)
         print("LM: ", materials)
         ideanest = uploadfilemodel.objects.filter(user_id = user, project_id = projectID)
         print("IN: ", ideanest)
         context = {
            'user' : user,
            'relations' : relations,
            'materials' : materials,
            'ideanest' : ideanest,
            'project' : project
         }
         return render(request, "Relations.html", context)
      except KeyError:
          # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
   def post(self, request):
      if request.method == 'POST':
         relationID = request.POST.get('myID')
         print("Relation ID: ", relationID)
         form = Relations(request.POST)
         user = request.session['id']
         name = request.POST.get('name')
         materials = request.POST.get('materials')
         ideanest = request.POST.get('ideanest')
         projectID = request.session['proj_id']
         if 'btnRelationCreate' in request.POST:
            form = Relations(user_id = user, name = name, materials_id = materials, ideafile_id = ideanest, project_id = projectID)
            form.save()
         elif 'btnRelationDelete' in request.POST:
            Relations.objects.get(id = relationID).delete()
            print('deleted successfully')
         elif 'btnLogout' in request.POST:
            try:
               del request.session['id'] #OR request.session.flush() to end session
            except KeyError:
               pass
            return redirect('LandingPage')
      return redirect('Relations')

## QUIZZZ
class CreateQuizView(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id']) 
         projectID = request.session['proj_id']
         #quiz = Quiz.objects.all()
         quiz = Quiz.objects.filter(user_id = user, project_id = projectID)
         #project = Project.objects.filter()
        # user = User.objects.all()
         context ={
            'quiz' : quiz,
            'user' : user
         }

         return render(request, "CreateQuiz.html", context)
      except KeyError: 
         # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
   def post(self, request):
      if request.method == 'POST':
         if 'btnCreate' in request.POST:
            try:
               form = Quiz(request.POST)
               user = request.session['id']
               name = request.POST.get('name')
               desc = request.POST.get('desc')
               date = request.POST.get('date')
               projectid = request.session['proj_id']
               #print(user)
               form = Quiz( quiz_name = name, quiz_date = date,user_id = user, quiz_desc = desc, project_id = projectid)
               form.save()
               quiz = Quiz.objects.filter(user_id = user).latest('id')
               request.session['quiz_id'] = quiz.id
               return redirect('EditQuiz')
               #print(form.errors)
            except:
               #messages.error(request, 'You must login before you can access this function')
               return redirect('CreateQuiz')
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
            return redirect('LandingPage')
      return redirect('CreateQuiz')

class EditQuizOptionsView(View):
   def get(self,request,question_id):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         user = User.objects.get(id = request.session['id']) 
         answer = Answer.objects.filter(question_id = question_id)
         question = Question.objects.get(id = question_id)
         #answer = Answer.objects.all()
         context ={
            'user' : user,
            'answer' : answer,
            'question' : question,
         }

         return render(request, "EditQuizOptions.html", context)
      except KeyError:
          # ------------------------------------------- SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
   def post(self,request,question_id):
      if request.method == 'POST':
         if 'btnDelete' in request.POST:
            answer = request.POST.get('a_id')
            print(answer)
            Answer.objects.get(id = answer).delete()
            print('deleted successfully')
            return redirect('EditQuiz')
         elif 'btnCreate' in request.POST:
            form = Answer(request.POST)
            answer = request.POST.get('ans')
            isAnswer = request.POST.get('isAnswer')
            if isAnswer == 'on':
               isAnswer = True
            else:
               isAnswer = False
            
            #if isAnswer == True and Answer.objects.filter(question_id = question_id, isAnswer = True).count > 0:
            #if isAnswer == True & Answer.objects.filter(question_id = question_id, isAnswer = True).exists:

             #  messages.error(request, 'Answer already exists! Add another option')
            #else:
            form = Answer( question_id = question_id, answer = answer, isAnswer = isAnswer)
            form.save()
            return redirect('EditQuiz')
         elif 'btnUpdate' in request.POST:
            id = request.POST.get('a_id')
            answer = request.POST.get('ans')
            isAnswer = request.POST.get('isAnswer')
            #print(user)
            if isAnswer == 'on':
               isAnswer = True
            else:
               isAnswer = False
            Answer.objects.filter(id = id).update(answer = answer, isAnswer = isAnswer)
            return redirect('EditQuiz')
#def EditQuizOptions(request, question_id):
#   question = Question.objects.get(id = question_id)
#   return render(request, "EditQuizOptions.html")  

class EditQuizView(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         print("-------Quiz in SESSION-------")
         print(request.session['quiz_id'])
         user = User.objects.get(id = request.session['id']) 
         quiz = Quiz.objects.get(id = request.session['quiz_id'])
         question = Question.objects.filter(quiz_id = request.session['quiz_id']).order_by('q_num')
         answer = Answer.objects.all()
         lastnum = Question.objects.filter(quiz_id = request.session['quiz_id']).order_by('-q_num')[:1]

         context ={
            'quiz' : quiz,
            'user' : user,
            'question' : question,
            'answer' : answer,
            'lastnum' : lastnum,
         }

         return render(request, "EditQuiz.html", context)
      except KeyError:
          # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
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
            #if isAnswer == True and Answer.objects.filter(question_id = q_id, isAnswer = True).exists:
            #   messages.error(request, 'Answer already exists! Add another option') 
            #   return redirect('EditQuiz')
            form = Answer( question_id = q_id, answer = option, isAnswer = isAnswer)
            form.save()

            return redirect('EditQuiz')
         elif 'btnUpdateQuestion' in request.POST:
            quiz = request.session['quiz_id']
            question = request.POST.get('q_id')
            num = request.POST.get('num') 
            q = request.POST.get('ques')
            #print(user)
            Question.objects.filter(id = question).update(q_num = num, question = q, quiz_id = quiz)
            return redirect('EditQuiz')
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
            return redirect('LandingPage')
      return redirect('EditQuiz')

def ViewQuiz(request):
   return render(request, "ViewQuiz.html")


class QuizView(View):
   def get(self,request):
      try:
         print(request.session['id'])
         print("-------USER in SESSION-------")
         print("-------Quiz in SESSION-------")
         print(request.session['quiz_id'])
         user = User.objects.get(id = request.session['id']) 
         quiz = Quiz.objects.get(id = request.session['quiz_id'])
         #question = Question.objects.all()
         question = Question.objects.filter(quiz_id = request.session['quiz_id']).order_by('q_num')
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
          # ------------------------------------------------ SHOW ALERT MESSAGE SA SIGNIN PAGE IF DILI NAKA LOG IN AG USER ----------------------------------#
         messages.error(request, 'You must login before you can access this function')
         return render(request, "Signin.html")
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
    form_class = EditForm
    template_name = 'LM_edit_materialdescriptions.html'

class DeleteMaterialDescriptionView(DeleteView):
    model = Materials
    template_name = 'LM_delete_materialdescription.html'
    context_object_name = 'mat'
    success_url = reverse_lazy('materials')