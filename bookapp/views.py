from django.shortcuts import render


def pageBooks(request):
    return render(request, "bookapp/books.html")

