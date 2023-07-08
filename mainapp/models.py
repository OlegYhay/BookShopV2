from django.db import models

import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from userapp.models import CustomUser


class Book(models.Model):
    class Meta:
        verbose_name = _('Книга')
        verbose_name_plural = _('Книги')
        ordering = ['title']
        db_table_comment = _('Книги для продажи')
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, verbose_name=_('Автор'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Цена'))
    cover = models.ImageField(upload_to='book/', blank=True, verbose_name=_('Фото'))
    category = models.ForeignKey("CategoryBooks", default='', null=True, on_delete=models.SET_DEFAULT,
                                 verbose_name=_('Категоиря'))
    description = models.TextField(default='without decription', null=True, verbose_name=_('Описание'))
    age_control = models.CharField(default='0+', null=True, max_length=20, verbose_name=_('Возрастное ограничение'))
    copyright = models.CharField(max_length=200, default='', null=True, verbose_name=_('Права'))
    ISBN = models.CharField(max_length=33, default='', null=True)
    is_popular = models.BooleanField(default=False, verbose_name=_('Популярное'))

    def __str__(self):
        return f'{self.title}({self.author})'

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})


class Author(models.Model):
    class Meta:
        verbose_name = _('Автор')
        verbose_name_plural = _('Авторы')

    name = models.CharField(max_length=120, verbose_name=_('Автор'))

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name = _('Отзывы')
        verbose_name_plural = _('Отзывы')
        ordering = ['date']

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    review = models.CharField(max_length=255, verbose_name='Комментарий')
    date = models.DateTimeField(verbose_name='Дата', auto_now=True)

    def __str__(self):
        return self.review


class CategoryBooks(models.Model):
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    name = models.CharField(max_length=255, verbose_name=_('Наименование'))

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
        ordering = ['date']

    class OrderStatus(models.TextChoices):
        NEW = _('Новый')
        Paid = _('Оплачено')
        Accepted = _('Принят')
        OnTheWay = _('В пути')
        Delivered = _('Доставлен')

    name = models.CharField(max_length=100, verbose_name=_('Имя'))
    secondname = models.CharField(max_length=100, verbose_name=_('Фамилия'))
    email = models.EmailField(verbose_name=_('Email'))
    fulladdress = models.CharField(max_length=255,
                                   verbose_name=_('Область(республика),город,улица,дом,квартира,индекс:'))
    notification = models.BooleanField(verbose_name=_('СМС уведомление о статусе заказа'), default=False)
    Payment = models.ForeignKey('Paymentmethod', on_delete=models.SET_NULL, null=True, verbose_name=_('Способ оплаты'))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('Покупатель'), blank=True)
    status = models.CharField(max_length=255, default=OrderStatus.NEW, choices=OrderStatus.choices,
                              verbose_name=_('Статус'), null=True, blank=True)
    date = models.DateTimeField(auto_now=True, verbose_name=_('Дата создания заказа'))

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': str(self.pk)})

    def __str__(self):
        return f'{self.name} {self.secondname}  {self.status}'


class OrderBooks(models.Model):
    class Meta:
        verbose_name = _('Состав заказа')

    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='books')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, verbose_name=_('Книга'))
    count = models.PositiveIntegerField(default=0, verbose_name=_('Количество'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Цена'))
    summ = models.PositiveIntegerField(default=0, verbose_name=_('Сумма'))


class Paymentmethod(models.Model):
    class Meta:
        verbose_name = _('Вид оплаты')
        verbose_name_plural = _('Виды оплат')

    name = models.CharField(max_length=100, verbose_name=_('Наименование'))

    def __str__(self):
        return self.name
