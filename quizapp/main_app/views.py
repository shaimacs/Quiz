from django.shortcuts import render
from .models import Quiz
from .models import Questions
from .models import Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
import json
import re



def index(request):
    return render(request, 'welcome.html')


def quiz_index(request):
    quiz = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quiz': quiz})

def quiz_show(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'quiz/show.html', {'quiz': quiz})


class QuizCreate(CreateView):
    model = Quiz
    fields = '__all__'
    success_url = '/quiz'


class QuestionsCreate(CreateView):
    model = Questions
    fields = '__all__'
    success_url = '/questions'


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/category'


class QuizUpdate(UpdateView):
    model = Quiz
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/quiz/' + str(self.object.pk))


class QuestionsUpdate(UpdateView):
    model = Questions
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/questions/' + str(self.object.pk))


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/category/' + str(self.object.pk))


class QuizDelete(DeleteView):
    model = Quiz
    success_url = '/quiz'


class QuestionsDelete(DeleteView):
    model = Questions
    success_url = '/questions'


class CategoryDelete(DeleteView):
    model = Category
    success_url = '/category'


def category(request):
    categories = []
    cat=''
    idd=[]
#fix this to (9,33)
    for i in range(9,14):
        response = requests.get('https://opentdb.com/api.php?amount=10&category={}&type=multiple'.format(i))
       
        # qus_data=response.json()
        id_response = requests.get('https://opentdb.com/api_category.php')
        id_res =json.loads(id_response.text)
        res =json.loads(response.text)

        for i in id_res['trivia_categories']:
            if(res["results"][0]["category"] == i['name']):
                idd=i['id']
                cat=i['name']
                if (len(res["results"]) < 1 ):
                    pass
                else:
                    categories.append({'name':res["results"][0]["category"],'id':idd})
                break

    # idd=8

    return render(request,'index.html',{
        'categories': categories,
        'id':idd,
        'name':cat
    })
    
def levels(request,id):

    return render(request,'levels.html',{'id':id})


def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = CreateUserForm()
        return render(request, 'signup.html', {'form': form})
    
def Profile(request, username):
    user = User.objects.get(username=username)
    quiz = Quiz.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'quiz': quiz})


def question(request,category_num,dif):
    options=set()
    response = requests.get('https://opentdb.com/api.php?amount=10&category={}&difficulty={}&type=multiple'.format(category_num,dif))
    res =json.loads(response.text)
    #put all answers in set 
    options.add(res['results'][0]['correct_answer'])

    for i in res['results'][0]['incorrect_answers']:
        options.add(i)

    question=res["results"][0]["question"]
    question = html_decode(question)
    return render(request, 'Questions.html',{
        'question':question,
        'options':options,
        'correct_answer':res['results'][0]['correct_answer']
        })

def html_decode(s):
  
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'),
            ("'", '&#039;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

def result(request):
    return render(request, 'Result.html')

def top_five(request):
    return render(request, 'top.html')

