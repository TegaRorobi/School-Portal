from django.urls import path
from .views import *

urlpatterns = [
    path('', UserCreateView.as_view(), name = 'user-create'),
    path('login/', UserLoginView.as_view(), name = 'user-login')
]
