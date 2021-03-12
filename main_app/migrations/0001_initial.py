# Generated by Django 3.1.7 on 2021-03-12 13:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название книги')),
                ('country', models.CharField(max_length=32, verbose_name='Страна')),
                ('genre', models.CharField(max_length=32, verbose_name='Жанр')),
                ('author', models.CharField(max_length=64, verbose_name='Автор')),
                ('year', models.CharField(max_length=32, verbose_name='Дата публикации')),
                ('description', models.TextField(verbose_name='Описание')),
                ('amount_in_stock', models.IntegerField(verbose_name='Имеющееся количество')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, verbose_name='Ваше имя:')),
                ('data', models.TextField(verbose_name='Поле для ответа:')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта для обратной связи:')),
            ],
        ),
        migrations.CreateModel(
            name='ClientsHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=64, verbose_name='Имя Фамилия')),
                ('date_of_issue', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выдачи')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bookmodel')),
            ],
        ),
    ]
