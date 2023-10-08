from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review

class ProductList(generic.ListView):
    model = Product


class ProductDetail(generic.DetailView):
    model = Product
# Create your views here.

class BrandList(generic.ListView):
    model = Brand