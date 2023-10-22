
from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review

def brand_list(request):
    data = Brand.objects.all()
    return render(request,'html',{'brand':data})
    
class ProductList(generic.ListView):
    model = Product


class ProductDetail(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
    


class BrandList(generic.ListView):
    model = Brand
    
class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    #override main query to get product for brand comming from url
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context