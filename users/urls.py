from django.urls import path
from .views import *

urlpatterns = [
    path('', UserCreateView.as_view(), name = 'user-create')
]