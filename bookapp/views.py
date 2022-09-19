from multiprocessing import context
from django.shortcuts import render
from .models import Book

def mainPage(request):
    book = Book.objects.all()

    context = {
        "book": book,
    }
    return render(request, "bookapp/mainPage.html", context)


def addBook(request):
    page = "add"
    context = {
        "page": page,
    }
    return render(request, "bookapp/add_edit.html", context)


def editBook(request):
    page = "edit"
    context = {
        "page": page,
    }
    return render(request, "bookapp/add_edit.html", context)


def deleteBook(request):
    return render(request, "bookapp/delete.html")