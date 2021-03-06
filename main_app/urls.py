from django.urls import path
from . import views


urlpatterns = [
    path('order_post/', views.order_post, name='order_post'),
    path('order_update/<int:pk>/', views.OrderUpdate.as_view(), name='order_update'),
    path('order_delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
    path('orders_list/', views.orders_list, name='orders_list'),

    path('history_post/<int:pk>/', views.history_post, name='history_post'),
    path('history_update/<int:pk>/', views.HistoryUpdate.as_view(), name='history_update'),
    path('history_delete/<int:pk>/', views.HistoryDelete.as_view(), name='history_delete'),

    path('book_post/', views.book_post, name='book_post'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('book_single/<int:id>/', views.book_single, name='book_single'),
    path('book_update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    path('books_list/', views.books_list, name='books_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
]