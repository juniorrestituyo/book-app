from django.db.models import Q
from .models import Book
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginationBooks(request, book, results):
    page = request.GET.get("page")
    paginator = Paginator(book, results)

    try: 
        book = paginator.page(number=page)
    except PageNotAnInteger:
        page = 1
        book = paginator.page(number=page)
    except EmptyPage:
        page = paginator.num_pages
        book = paginator.page(number=page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, book


def searchBook(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
        
    book = Book.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(author__icontains=search_query)
    )

    return book, search_query