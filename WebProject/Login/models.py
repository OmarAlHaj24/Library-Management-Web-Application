from django.db import models

# Create your models here.
class users(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class Admin(models.Model):
    Admin=models.ForeignKey(users, on_delete=models.CASCADE)

