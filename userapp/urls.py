from django.urls import path
from .views import *

urlpatterns = [
    path('registration/login/', LoginUserView.as_view(), name='login'),
    path('registration/logout/', LogoutUserView.as_view(), name='logout'),
    path('registration/create_user/', CreateUserView.as_view(), name='create_user'),
]
