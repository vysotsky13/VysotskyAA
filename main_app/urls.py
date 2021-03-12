from django.urls import path
from . import views


urlpatterns = [
    path('book_post/', views.book_post, name='book_post'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('book_single/<int:id>/', views.book_single, name='book_single'),
    path('book_update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    path('books_list/', views.books_list, name='books_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
]