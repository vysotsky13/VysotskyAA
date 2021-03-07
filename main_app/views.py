from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import BookModel
from .forms import ResponseForm, BookForm


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
    context = {
        'q': book_query,
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

