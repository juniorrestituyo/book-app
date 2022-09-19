from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from .utils import searchBook, paginationBooks
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    return render(request, "bookapp/home.html")


def mainPage(request):
    book, search_query = searchBook(request)

    custom_range, book = paginationBooks(request, book, 5)

    context = {
        "book": book,
        "search_query": search_query,
        "custom_range": custom_range,
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
        if form.is_valid():
            form.save()
            return redirect("mainPage")

    context = {
        "page": page,
        "form": form,
    }
    return render(request, "bookapp/add_edit.html", context)


def editBook(request, pk):
    page = "edit"
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("mainPage")

    context = {
        "page": page,
        "form": form,
        "book": book,
    }
    return render(request, "bookapp/add_edit.html", context)


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == "POST":
        book.delete()
        return redirect("mainPage")

    return render(request, "bookapp/delete.html")