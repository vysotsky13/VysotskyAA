from django.db import models
from django.urls import reverse
from django.utils import timezone


class ResponseModel(models.Model):
    user = models.CharField(max_length=32, verbose_name='Ваше имя:')
    data = models.TextField(verbose_name='Поле для ответа:')
    email = models.EmailField(verbose_name='Почта для обратной связи:')

    def __str__(self):
        return 'Ответ пользователя ' + self.user


class BookModel(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название книги')
    country = models.CharField(max_length=32, verbose_name='Страна')
    genre = models.CharField(max_length=32, verbose_name='Жанр')
    author = models.CharField(max_length=64, verbose_name='Автор')
    year = models.CharField(max_length=32, verbose_name='Дата публикации')
    description = models.TextField(verbose_name='Описание')
    amount_in_stock = models.IntegerField(verbose_name='Имеющееся количество')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_single', args=[self.id])


class ClientsHistoryModel(models.Model):
    book = models.ForeignKey('BookModel', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64, verbose_name='Имя Фамилия')
    date_of_issue = models.DateTimeField(default=timezone.now, blank=False, verbose_name='Дата выдачи')
    return_date = models.DateTimeField(blank=True, verbose_name='Дата возврата', null=True)

    def __str__(self):
        return 'История пользования ' + self.full_name

    def get_absolute_url(self):
        return reverse('book_single', args=[self.book.id])
