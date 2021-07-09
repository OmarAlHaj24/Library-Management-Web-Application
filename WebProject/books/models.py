import datetime

from django.db import models
from django.utils.timezone import timezone
# Create your models here.
class books(models.Model):
    bookname = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_year = models.DateTimeField(auto_now_add=False,auto_now=False)
    def __str__(self):
        return self.bookname
