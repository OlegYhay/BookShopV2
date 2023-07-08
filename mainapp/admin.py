from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['author', 'price']
    fieldsets = (
        (_('Основная информация'), {
            'fields': ['title', 'author', 'price', 'description']
        }),
        (_('Дополнительная информация'), {
            'fields': ['cover', 'category', 'age_control', 'copyright', 'ISBN', 'is_popular']
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'date']
    list_filter = ['user', 'status']
    fieldsets = (
        (_('Основная информация'), {
            'fields': ['name', 'secondname', 'email', 'fulladdress']
        }),
        (_('Дополнительная информация'), {
            'fields': ['notification', 'Payment', 'user', 'status']
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'review', 'author']


@admin.register(CategoryBooks)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderBooks)
class OrderBooksAdmin(admin.ModelAdmin):
    pass


@admin.register(Paymentmethod)
class PaymentmethodAdmin(admin.ModelAdmin):
    pass
