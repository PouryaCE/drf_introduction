from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} - {self.body[:20]}.... '