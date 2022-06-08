from dataclasses import field
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
# Create your models here.

class Book(models.Model):
    bookName = models.CharField(max_length=30, null=True, blank=True)
    bookAuthor = models.CharField(max_length=20)
    bookType = models.IntegerField(default=1)
    _id=models.AutoField(primary_key=True,editable=False)
    field=['_id', 'bookName', 'bookType']
    def __str__(self):
        return self.bookName
