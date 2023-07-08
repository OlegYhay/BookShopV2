from django.urls import path
from .views import *

urlpatterns = [
    path('', Main_page.as_view(), name='main_page'),
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<uuid:id>', BookDetail.as_view(), name='book_detail'),
    path('cart/change/', login_required(CartView.as_view(), login_url=reverse_lazy('login')), name='cart_change'),
    path('my_cart/', login_required(CartView.as_view(), login_url=reverse_lazy('login')), name='my_cart'),
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_create_success/', OrderCreateSuccess.as_view(), name='order_create_succes'),
    path('order_list/', login_required(OrderListView.as_view(), login_url=reverse_lazy('login')), name='order_list'),
    path('dilivery/', DiliveryTemplateView.as_view(), name='dilivery'),
    path('search_result/', BookSearchList.as_view(), name='search_results')
]
