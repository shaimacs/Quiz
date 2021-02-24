from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz_index, name='quiz_index'),
    path('quiz/<int:quiz_id>/', views.quiz_show, name='quiz_show'),
    path('quiz/create/', views.QuizCreate.as_view(), name='quiz_create'),
    path('quiz/<int:pk>/update/', views.QuizUpdate.as_view(), name='quiz_update'),
    path('quiz/<int:pk>/delete/', views.QuizDelete.as_view(), name='quiz_delete'),
    path('levels/question/<int:category_num>/<dif>/', views.question, name='question'),
    path('questions/create/', views.QuestionsCreate.as_view(), name='questions_create'),
    path('questions/<int:pk>/update/', views.QuestionsUpdate.as_view(), name='questions_update'),
    path('questions/<int:pk>/delete/', views.QuestionsDelete.as_view(), name='questions_delete'),
    path('questions/', views.questionsShow, name='questions_show'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.Profile, name='profile'),
    path('category/', views.category, name='category'),
    path('result/<int:score>/<category>', views.result, name='result'),
    path('levels/', views.levels, name='levels'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),{'post_reset_redirect': 'reset_password_done'}, name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    path('levels/<int:id>', views.levels, name='levels'),
    # path('top_five/', views.top_five, name='top_five'),
    path('top_five/<category>', views.top_five, name='top_five'),
    path('sei/', views.sei, name='sei'),
    path('category_top_five/', views.category_top_five, name='category_top_five')

]