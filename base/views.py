from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, BookSerializer, Loan,LoanSerializer
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def books(request, id=0):
    if request.method=='GET':
        if int(id)>0:
            if int(id)>Book.objects.count():#return error if index is greater than items in the list
                return JsonResponse({'ERROR':'INDEX OUT OF RANGE'})
            book=Book.objects.all()[int(id)-1]
            res=BookSerializer().getBook(book)
            return JsonResponse(res,safe=False)
        else:#return everything
            bookList=[]
            for bookItem in Book.objects.all():
                bookList.append({
                    'Book_Name':bookItem.bookName,
                    'Book_Author':bookItem.bookAuthor,
                    'BookID':bookItem._id
                })
            return JsonResponse(bookList,safe=False)

    if request.method=='POST':
        Book.objects.create(bookName=request.data['Book_Name'],bookAuthor=request.data['Book_Author'])            
        return JsonResponse({'Book added':'Success'})

    if request.method=='DELETE':
        bookDel=Book.objects.get(_id=id)
        bookDel.delete()
        return JsonResponse({'Book Deleted':'Success'})

    if request.method=='PUT':
        bookVar=Book.objects.all()[int(id)-1]
        bookVar.bookName = request.data['Book_Name']
        bookVar.bookAuthor=request.data['Book_Author']
        bookVar.save()
        return JsonResponse({'Book Updated':'Success'})

    return HttpResponse ("This is the books section")

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def loans(request,id=0):
    if request.method=='GET':
        if int(id)>0:
            if int(id)>Loan.objects.count():
                return JsonResponse({'INDEX ERROR':'OUT OF RANGE'})
            loan=Loan.objects.all()[int(id)-1]
            res=LoanSerializer().getLoan(loan)
            return JsonResponse(res,safe=False)
        else:
            loanList=[]
            for loanItem in Loan.objects.all():
                loanList.append({
                    'userID':loanItem.userID.id,
                    'userName':str(loanItem.userID),
                    'bookID':loanItem.bookID._id,
                    'bookName':str(loanItem.bookID.bookName)
                })
            return JsonResponse(loanList, safe=False)
    if request.method=='POST':
        user=User.objects.get(first_name=request.data['userName'])
        book=Book.objects.get(book=request.data['bookName'])
        Loan.objects.create(userID=user,bookName=book)
        return JsonResponse(request.data)

    if request.method=='DELETE':
        loanDelete=Loan.objects.delete(_id=id)
        loanDelete.delete()
        return JsonResponse({'method':'DELETE'})
    if request.method=='PUT':
        return JsonResponse({'method':'PUT'})