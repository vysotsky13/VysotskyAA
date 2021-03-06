from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from .models import BookModel, ClientsHistoryModel, Order
from .forms import ResponseForm, BookForm, ClientsHistoryForm, OrderForm


def index(request):
    return render(request, 'base.html', context={})


def contacts(request):
    form = ResponseForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/contacts/')
    context = {
        'form': form,
    }
    return render(request, "other/contacts.html", context)


def book_single(request, id):
    book_query = get_object_or_404(BookModel, id=id)
    histories_query = ClientsHistoryModel.objects.all().filter(book=book_query)
    context = {
        'q': book_query,
        'histories': histories_query,
    }
    return render(request, "books/book_single.html", context)


def books_list(request):
    qs = BookModel.objects.all().order_by('title')
    paginator = Paginator(qs, 50)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
    }
    return render(request, "books/books_list.html", context)


class SearchView(ListView):
    model = BookModel
    template_name = 'books/search.html'
    context_object_name = 'books'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         country__contains=self.request.GET['country'],
                                         author__contains=self.request.GET['author'])


def book_post(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/books_list/')
    context = {
        'form': form,
    }
    return render(request, "books/book_post.html", context)


def history_post(request, pk):
    book_query = get_object_or_404(BookModel, id=pk)
    form = ClientsHistoryForm(request.POST or None)
    form.initial = {'book': book_query}
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/books_list/')
    context = {
        'form': form,
    }
    return render(request, "history/history_post.html", context)


class BookUpdate(UpdateView):
    template_name = 'books/book_post.html'
    model = BookModel
    form_class = BookForm


class HistoryUpdate(UpdateView):
    template_name = 'history/history_post.html'
    model = ClientsHistoryModel
    form_class = ClientsHistoryForm


class BookDelete(DeleteView):
    model = BookModel
    success_url = reverse_lazy('books_list')
    template_name = 'books/confirm_book_delete.html'


class HistoryDelete(DeleteView):
    model = ClientsHistoryModel
    success_url = reverse_lazy('books_list')
    template_name = 'history/confirm_history_delete.html'


class OrderUpdate(UpdateView):
    template_name = 'orders/order_post.html'
    model = Order
    form_class = OrderForm


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders_list')
    template_name = 'orders/confirm_order_delete.html'


def order_post(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/orders_list/')
    context = {
        'form': form,
    }
    return render(request, "orders/order_post.html", context)


def orders_list(request):
    qs = Order.objects.all()
    pagination = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        qs = pagination.page(page)
    except PageNotAnInteger:
        qs = pagination.page(1)
    except EmptyPage:
        qs = pagination.page(pagination.num_pages)

    context = {
        'query': qs,
    }
    return render(request, "orders/order_list.html", context)

