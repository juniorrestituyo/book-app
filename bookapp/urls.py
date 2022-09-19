from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainPage, name="mainPage"),
    path("add/", views.addBook, name="add-book"),
    path("edit/", views.editBook, name="edit-book"),
    path("delete/", views.deleteBook, name="delete-book"),
]