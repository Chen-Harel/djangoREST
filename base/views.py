from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
# Create your views here.

def index(req):
    return HttpResponse('<h1>Hello, World!</h1>')

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def books(req, id=0):
    if req.method=='GET':
        if int(id)>0:
            if int(id)>Book.objects.count():#return error if index is greater than items in the list
                return JsonResponse({'ERROR':'INDEX OUT OF RANGE'})
            book=Book.objects.all()[int(id)-1]
            return JsonResponse({#return one item if index(id) is OK
                'Book Name':book.bookName,
                'Book Author':book.bookAuthor,
                'BookID':book._id
            },safe=False)
        else:#return everything
            bookList=[]
            for bookItem in Book.objects.all():
                bookList.append({
                    'Book Name':bookItem.bookName,
                    'Book Author':bookItem.bookAuthor,
                    'BookID':bookItem._id
                })
            return JsonResponse(bookList,safe=False)

    if req.method=='POST':
        Book.objects.create(bookName=req.data['Book Name'],bookAuthor=req.data['Book Author'])            
        return JsonResponse({'Book added':'Success'})

    if req.method=='DELETE':
        bookDel=Book.objects.get(_id=id)
        bookDel.delete()
        return JsonResponse({'Book Deleted':'Success'})

    if req.method=='PUT':
        bookVar=Book.objects.all()[int(id)-1]
        bookVar.bookName = req.data['Book Name']
        bookVar.bookAuthor=req.data['Book Author']
        bookVar.save()
        return JsonResponse({'Book Updated':'Success'})

    return HttpResponse ("This is the books section")