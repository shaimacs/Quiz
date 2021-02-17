from django.contrib import admin
from .models import Quiz
from .models import Questions
from .models import Category


# Register your models here.
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Category)