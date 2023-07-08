import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from userapp.models import CustomUser
from .forms import OrderCustomForm
from .models import Book, Review, Order


# Create your views here.

class Main_page(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(is_popular=True)
        return context


class BookList(ListView):
    model = Book
    template_name = "book_list.html"
    paginate_by = 8
    context_object_name = 'books'


class BookSearchList(ListView):
    model = Book
    template_name = "search_book_list.html"
    paginate_by = 8
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        result = Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(BookSearchList, self).get_context_data(**kwargs)
        if len(data['books']) == 0:
            data['mistake'] = 'Ничего не найдено!'
        return data


class BookDetail(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = 'book'
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(book=self.object)

        return context

    def post(self, request, *args, **kwargs):
        book, comment = self.get_object(), request.POST['comment']
        new_comment = Review.objects.create(book=book,
                                            author=request.user,
                                            review=comment)
        new_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_cart(request):
    cart, itogsumm = {}, 0
    cart_list = request.session.get('cart', {})
    for key, value in cart_list.items():
        book = Book.objects.get(id=key)
        sum = value * book.price
        cart[key] = {
            'product': book,
            'quantity': value,
            'total_price': sum,
        }
        itogsumm += sum
    return {'cart': cart, 'itogsumm': itogsumm}


class CartView(View):
    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        id, count_add = request.POST['book'], request.POST['count']
        count = cart.get(id, 0)
        cart[id] = count + int(count_add)
        if cart[id] <= 0:
            del cart[id]
        request.session['cart'] = cart
        request.session.modified = True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def get(self, request, *args, **kwargs):
        cart = get_cart(request)
        can_order = False if cart['itogsumm'] <= 0 else True
        cart['can_order'] = can_order
        return render(request, 'cart_list.html', cart)


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    success_url = reverse_lazy('order_create_succes')
    fields = '__all__'

    def get_initial(self, form_class=None):
        initial = super().get_initial()
        initial['name'] = self.request.user.first_name
        initial['secondname'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        initial['user'] = self.request.user
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_summ = get_cart(self.request)
        context['cart'] = cart_summ['cart']
        context['itogsumm'] = cart_summ['itogsumm']
        return context


class OrderCreateSuccess(TemplateView):
    template_name = 'order_create_success.html'

    def dispatch(self, request, *args, **kwargs):
        del request.session['cart']
        return super().dispatch(request, *args, **kwargs)


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order_list.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class DiliveryTemplateView(TemplateView):
    template_name = 'dilivery.html'
