from django.urls import path
from . import views


urlpatterns = [
    path('book_single/<int:id>/', views.book_single, name='book_single'),
    path('books_list/', views.books_list, name='books_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
]