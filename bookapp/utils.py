from django.db.models import Q
from .models import Book

def searchBook(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
        
    book = Book.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(author__icontains=search_query)
    )

    return book, search_query