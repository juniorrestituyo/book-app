from django.shortcuts import render


def mainPage(request):
    return render(request, "bookapp/books.html")


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