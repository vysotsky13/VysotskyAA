from django.db import models
from django.urls import reverse_lazy


class ResponseModel(models.Model):
    user = models.CharField(max_length=32, verbose_name='Ваше имя:')
    data = models.TextField(verbose_name='Поле для ответа:')
    email = models.EmailField(verbose_name='Почта для обратной связи:')

    def __str__(self):
        return 'Ответ пользователя ' + self.user
