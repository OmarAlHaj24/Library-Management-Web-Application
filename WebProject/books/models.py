from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Book(models.Model):
    bookname = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50, primary_key=True)
    author = models.CharField(max_length=50)
    PublishDate = models.DateTimeField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.bookname


def tenDays():
    return timezone.now() + timezone.timedelta(days=10)


class Booking(models.Model):
    bookedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    bookedBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowingPeriod = models.DateField(default=tenDays)
    id = models.IntegerField(primary_key=True)

    # class Meta:
    #     unique_together = (
    #         ('bookedBy', 'bookedBook'),
    #     )

    def __str__(self):
        return str(self.bookedBy) + " booked " + str(self.bookedBook)
