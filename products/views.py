
from django.shortcuts import render
from django.views import generic
from .models import Product , Brand , Review
#from django.db.models import Q , Value , F
#from django.db.models.aggregates import Count,Min,Max,Avg,Sum



def brand_list(request):
    data = Brand.objects.all()
    return render(request,'html',{'brand':data})



def mydebug(request):
    #data = Product.objects.select_related('brand').all()
    #data = Product.objects.filter(price__gt=90) we change with it the loop in page debug.html to 'object.price'
    #data = Product.objects.filter(price__lt=90)
    #data = Product.objects.filter(price__lte=90) less or greater
    #data = Product.objects.filter(price__range=(20,22))
    #data = Product.objects.filter(brand__id__gt = 50) to get information from another model
    #data = Product.objects.filter(name__contains = 'Hill')
    #data = Product.objects.filter(name__startswith = 'Denise')
    #data = Product.objects.filter(name__endswith = 'Hill')
    #data = Product.objects.filter(name__isnull = True)
    #data = Product.objects.filter(price__gte =80 , name__endswith = 'Hill') if we have two conditions
    #data = Product.objects.filter(
    #     Q(price__gte = 99) |
    #     Q(name__endswith = 'Hill')
    #) we added a line above to import Q and we use & when we want both condition and | when want only one condition
    #data = Product.objects.order_by('price')
    #data = Product.objects.order_by('-price')
    #data = Product.objects.order_by('name','-price')
    #data = Product.objects.filter(flag='New').order_by('-price')
    #data = Product.objects.order_by('price')[0]  [-1] but we need here to delete the for loop in debug.html
    #data = Product.objects.earliest('price')
    #data = Product.objects.latest('price')
    #data = Product.objects.all()[:10] to get elements from 1 to 10
    #data = Product.objects.values('name','flag') but here we have to change object to object.name in the debug.html loop and the advantage we notice that in SQL brings back two colons
    #data = Product.objects.only('name','flag') here we must add{{object.brand}} to loop in debug.html but it's heavy
    #data = Product.objects.defer('quantity') to get all lines and leave a line from the model
    #data = Product.objects.select_related('brand').all() # foreignkey , one-to-one this make query lighter
    #data = Product.objects.prefetch_related('brand').all() # many to many
    
    
    
        # aggregation : min max sum avg count we have to import a lone above
    # data = Product.objects.aggregate(myavg = Avg('price'))
    # data = Product.objects.aggregate(Count('quantity'))
    # data = Product.objects.aggregate(Count('id'))
    
    # data = Product.objects.aggregate(Sum('quantity'))
    
    # data = Product.objects.aggregate(Min('price'))
    
    data = Product.objects.all()
    return render(request,'products/debug.html',{'data':data})
    
class ProductList(generic.ListView):
    model = Product
    paginate_by=50


class ProductDetail(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
    


class BrandList(generic.ListView):
    model = Brand
    paginate_by=50
    
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