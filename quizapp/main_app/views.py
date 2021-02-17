from django.shortcuts import render
from .models import Quiz
from .models import Questions
from .models import Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests
import json


def index(request):
    return render(request, 'index.html')

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


def test(request):
    categories = []

    for i in range(1,33):
        response = requests.get('https://opentdb.com/api.php?amount=10&category={}&difficulty=easy&type=multiple'.format(i))
        # qus_data=response.json()
        res =json.loads(response.text)
        if (len(res["results"]) < 1 ):
            pass
        else:
            categories.append(res["results"][0]["category"])
        
    return render(request,'test.html',{
        'categories': categories
    })

def category(request):
     return render(request,'category.html')




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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
