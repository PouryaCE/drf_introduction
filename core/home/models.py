from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    name  = models.CharField(max_length=30)
    age   = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name




class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user.username} - {self.title} - {self.body[:20]}'



class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()


    def __str__(self):
        return f"{self.user.username} - {self.question.title} - {self.question.body[:20]}"
