from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField()
    Time = models.IntegerField()
    winStreak = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Questions(models.Model):
    question = models.CharField(max_length=400)
    type = models.CharField(max_length=150)
    correctAnswer = models.CharField(max_length=150)
    Level = models.CharField(max_length=150)
    hint = models.CharField(max_length=150)
    # time = models.DateTimeField(auto_now_add=False, blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Score(models.Model):
    score = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



