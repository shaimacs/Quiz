from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('quiz/', views.quiz_index, name='quiz_index'),
    path('quiz/<int:quiz_id>/', views.quiz_show, name='quiz_show'),
    path('quiz/create/', views.QuizCreate.as_view(), name='quiz_create'),
    path('quiz/<int:pk>/update/', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('question/', views.question, name='question'),
    path('questions/create/', views.QuestionsCreate.as_view(), name='questions_create'),
    path('questions/<int:pk>/update/', views.QuestionsUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionsDelete.as_view(), name='questions_delete'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.Profile, name='profile'),
    path('category/', views.category, name='category'),
    path('levels/', views.levels, name='levels')
]
