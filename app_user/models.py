from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.TextField(max_length=12)
    email = models.EmailField()
    created_in = models.DateTimeField(auto_now_add= True)