from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def mainPage(request):
    book = Book.objects.all()

    context = {
        "book": book,
    }
    return render(request, "bookapp/mainPage.html", context)


def viewBook(request, pk):
    book = Book.objects.get(id=pk)

    context = {
        "book": book,
    }
    return render(request, "bookapp/view_book.html", context)


def addBook(request):
    page = "add"
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        
        return redirect("mainPage")

    context = {
        "page": page,
        "form": form,
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