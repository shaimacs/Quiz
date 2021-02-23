# from quizapp.main_app.templates.main_app.forms import ScoreForm
from django.shortcuts import redirect, render
from .models import Quiz
from .models import Questions
from .models import Category
from .models import Score
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import LoginForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
import requests
import json


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
    response = requests.get('https://opentdb.com/api.php?amount=5&category={}&difficulty={}&type=multiple'.format(category_num,dif))
    res =json.loads(response.text)
    #put all answers in set 
    qq={
    "q1":res['results'][0],
    "q2":res['results'][1],
    "q3":res['results'][2],
    "q4":res['results'][3],
    "q5":res['results'][4]
    }
    options.add(html_decode(res['results'][0]['correct_answer']))
    for i in res['results'][0]['incorrect_answers']:
        print(i,'555555555555555555555555')
        options.add(html_decode(i))
    question=res["results"][0]["question"]
    question = html_decode(question)
    print(options,'888888888888888888888888')
    # newOP={"zzzz"} 
    # for i in options:
    #     options.add(html_decode(i))
    # print('qqqqqqq',question)
    # print('oooooooooooo',options)
    # print('op',newOP)
    return render(request, 'Questions.html',{
        'question':question,
        'options':options,
        'correct_answer':res['results'][0]['correct_answer'],
        'category':res["results"][0]["category"],
        'qq':qq,
        'category_num':category_num,
        'dif':dif
        })

# def question(request,category_num,dif):
#     options=set()
#     # options2=set()
#     x=0
#     questions_list=[]
#     response = requests.get('https://opentdb.com/api.php?amount=5&category={}&difficulty={}&type=multiple'.format(category_num,dif))
#     res =json.loads(response.text)
#     #put all answers in set 
#     for i in range(5):

#         options.add(res['results'][i]['correct_answer'])
#         for x in res['results'][i]['incorrect_answers']:
#             options.add(x)

#         question=res["results"][i]["question"]
#         question =html_decode(question)
#         questions_list.append({'q':question,'options':options})

#     # for i in options:
#     #     options2.add(html_decode(i))

#     return render(request, 'Questions.html',{
#         'questions':questions_list,
#         'options':options,
#         'x':x,
#         'correct_answer':res['results'][0]['correct_answer'],
#         'category':res["results"][0]["category"]
#         })

def html_decode(s):
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'),
            ("'", '&#039;'), 
            ("-", '&shy;'),
            ("ñ", '&ntilde;'),
            ("µ", '&micro;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s



def result(request,no,category):
    current_user = request.user

    c = Category.objects.get(name=category)
    c_id = c.id

    Score.objects.filter(Q(user_id=current_user.id), Q(category_id = c_id)).update(score=no)

    #to get user's score
    e = Score.objects.get(Q(user_id=current_user.id), Q(category_id = c_id))
    score = e.score
            
    return render(request, 'Result.html',{
        'no':score,
        'category':category
    })

def top_five(request):
    users = Score.objects.order_by('-score')

    return render(request, 'top.html',{
        'user1':users[0],
        'user2':users[1],
        'user3':users[2],
        'user4':users[3],
        'user5':users[4],
        })



    