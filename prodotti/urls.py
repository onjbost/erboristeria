from django.contrib import admin
from django.urls import path, include
from .import views
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", home, name='home'),
    path("shopping/", ShopView.as_view(), name="shop"),
    path('prodotto/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('preventivo/', preventivo, name='preventivo'),
    path('su_di_noi/', about, name='about'),
    path('termini_di_servizio/', service, name='service'),
    path('privacy_policy/', privacy, name='privacy')
]