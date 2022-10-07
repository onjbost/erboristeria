from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
       path('register/', UserRegisterView.as_view(), name='register'),
       path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
       path('password/', PasswordsChangeView.as_view(),name='change-password'),
       path('changed_password', password_success, name='password-done'),
       path('settings/', account, name="account"),
]
