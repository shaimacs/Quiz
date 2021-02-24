from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField()
    Time = models.IntegerField()
    winStreak = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Questions(models.Model):
#     category = models.CharField(max_length=150)
#     type = models.CharField(max_length=150)
#     difficulty = models.CharField(max_length=150)
#     question = models.CharField(max_length=400)
#     correct_answer = models.CharField(max_length=150)
#     incorrect_answers = ArrayField(models.CharField(max_length=200), blank=True)
#     # hint = models.CharField(max_length=150)
#     # time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
#     def __str__(self):
#         return self.question

class Category(models.Model):
    name = models.CharField(max_length=150)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        
        return self.name

class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Questions(models.Model):
    # category = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    difficulty = models.CharField(max_length=150)
    question = models.CharField(max_length=400)
    correct_answer = models.CharField(max_length=150)
    incorrect_answers = ArrayField(models.CharField(max_length=200), blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # hint = models.CharField(max_length=150)
    # time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        
        return self.question
   
    # def to_dict(self):
    #     return self.__dict__
    
    def __repr__(self):
        return (self.question+','+self.correct_answer+',' +self.incorrect_answers[0]+',' +self.incorrect_answers[1]+',' +self.incorrect_answers[2])


