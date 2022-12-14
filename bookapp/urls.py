from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.mainPage, name="mainPage"),
    path("add/", views.addBook, name="add-book"),
    path("view/<str:pk>/", views.viewBook, name="view-book"),
    path("edit/<str:pk>/", views.editBook, name="edit-book"),
    path("delete/<str:pk>/", views.deleteBook, name="delete-book"),
]