from django.db import models
from django.urls import reverse


class ResponseModel(models.Model):
    user = models.CharField(max_length=32, verbose_name='Ваше имя:')
    data = models.TextField(verbose_name='Поле для ответа:')
    email = models.EmailField(verbose_name='Почта для обратной связи:')

    def __str__(self):
        return 'Ответ пользователя ' + self.user


class BookModel(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название книги')
    county = models.CharField(max_length=32, verbose_name='Страна')
    genre = models.CharField(max_length=32, verbose_name='Жанр')
    author = models.CharField(max_length=64, verbose_name='Автор')
    year = models.CharField(max_length=32, verbose_name='Дата публикации')
    amount_in_stock = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_single', args=[self.id])
