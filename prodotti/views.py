from audioop import reverse
from this import d
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from prodotti.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'landing-page/index.html', {})


class ShopView(ListView):
    model = Product
    template_name = 'shop/index.html'
    
    
class ArticleDetailView(DetailView):
    model = Product
    template_name = 'article_detail/index.html'
    
    
def preventivo(request):
    return render(request, 'preventivo.html', {})


def about(request):
    return render(request,'about/index.html', {} )

def service(request):
    return render(request, 'privacyeservice/service.html', {})

def privacy(request):
    return render(request, 'privacyeservice/privacy.html', {})

