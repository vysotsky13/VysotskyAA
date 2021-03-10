from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import BookModel


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        BookModel.objects.create(title='Book', country='Country', genre='Genre',
                                 author='Author', year='Year', description='Description',
                                 amount_in_stock=1)

    def test_get_absolute_url(self):
        book = BookModel.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/book_single/1/')

    def test_instance(self):
        book = BookModel(title='Book', country='Country')
        self.assertTrue(isinstance(book, BookModel))

    def test_title_and_label(self):
        book = BookModel.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название книги')

    def test_company_name_and_label(self):
        job = BookModel.objects.get(id=1)
        field_label = job._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'Страна')

    def test_description_and_label(self):
        book = BookModel.objects.get(id=1)
        field_label = book._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_author_and_label(self):
        book = BookModel.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'Автор')
