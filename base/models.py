from dataclasses import field
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from rest_framework import serializers
# Create your models here.

class Book(models.Model):
    bookName = models.CharField(max_length=30, null=True, blank=True)
    bookAuthor = models.CharField(max_length=20)
    bookType = models.IntegerField(default=1)
    _id=models.AutoField(primary_key=True,editable=False)
    field=['_id', 'bookName', 'bookType']
    def __str__(self):
        return self.bookName

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['bookName', 'bookAuthor', '_id']
    
    def getBook(self, obj):
        return {
            'bookName':obj.bookName,
            'bookAuthor':obj.bookAuthor,
            '_id':obj._id
        }

class Loan(models.Model):
    userID=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bookID=models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    field=['userID', 'bookID']
    def __str__(self):
        return str(self.userID)

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=['userID', 'bookID']
    
    def getLoan(self, obj):
        return {
            'userID':obj.userID.id,
            'userName':str(obj.userID),
            'bookID':obj.bookID._id,
            'bookName':str(obj.bookID)
        }