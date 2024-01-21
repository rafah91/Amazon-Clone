from django.shortcuts import render , redirect
from django.views import generic
from .models import Product , Brand , Review

from django.db.models import Q , Value , F
from django.db.models.aggregates import Count,Min,Max,Avg,Sum
from django.views.decorators.cache import cache_page
from django.utils import translation

from .tasks import send_emails
from django.http import JsonResponse
from django.template.loader import render_to_string

def brand_list(request):
    data = Brand.objects.all()  # query --> method --> change data main query 
    return render(request,'html',{'brands':data}) # {'brands':data} --> context method(extra data) , html = template


# @cache_page(60 * 1)
def mydebug(request):
    # data = Product.objects.filter(price__gte=100)
    # data = Product.objects.filter(price__lte=100)
    # data = Product.objects.filter(price__range=(20,22))
    
    # data = Product.objects.filter(brand__id__gt = 50)
    
    # data = Product.objects.filter(name__contains = 'Hill')
    # data = Product.objects.filter(name__startswith = 'Denise')
    # data = Product.objects.filter(name__endswith = 'Hill')
    # data = Product.objects.filter(name__isnull = True)
    
    # data = Product.objects.filter(price__gte =80 , name__endswith = 'Hill')
    
    # data = Product.objects.filter(
    #     Q(price__gte = 99) |
    #     Q(name__endswith = 'Hill')
    # )
    
    # data = Product.objects.order_by('price')
    # data = Product.objects.order_by('-price')
    # data = Product.objects.order_by('name','-price')
    # data = Product.objects.filter(flag='New').order_by('-price')
    
    # data = Product.objects.order_by('price')[0]  [-1]
    # data = Product.objects.earliest('price')
    # data = Product.objects.latest('price')
    # data = Product.objects.all()[:10]
    
    # data = Product.objects.values('name','flag')
    # data = Product.objects.only('name','flag')
    # data = Product.objects.defer('quantity')
    
    # data = Product.objects.select_related('brand').all()   # foreignkey , one-to-one
    # data = Product.objects.prefetch_related('brand').all()   # many to many
    
    # aggregation : min max sum avg count
    # data = Product.objects.aggregate(myavg = Avg('price'))
    # data = Product.objects.aggregate(Count('quantity'))
    # data = Product.objects.aggregate(Count('id'))
    
    # data = Product.objects.aggregate(Sum('quantity'))
    
    # data = Product.objects.aggregate(Min('price'))
    
    
    # data = Product.objects.annotate(price_with_tax=F('price')*1.25)
    
    
    data = Product.objects.all()
    
    # data = User.objects.all()  # [1,2,3,4 ....... n]
    
    # execute function : task 
    send_emails.delay(data) # run task  : time 20 sec
    
    return render(request,'products/debug.html',{'data':data})




class ProductList(generic.ListView):
    model = Product
    paginate_by = 50
    
    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
    #         lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
    #         translation.activate(lang)
    #     return queryset    

    
class ProductDetail(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()) 
        return context
    
    
    
class BrandList(generic.ListView):
    model = Brand
    paginate_by = 50
    
    
    
class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'
    
    # ovveride main query to get products for brand comming from url 
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    


def add_product_review(request,slug): #any function we want to use ajax in it we need to do it with function not in a class
    
    product = Product.objects.get(slug=slug)
    review = request.POST['user_review']
    rate = request.POST['rating']
    
    Review.objects.create(
        user=request.user,
        product = product , 
        rate = rate,
        feedback = review
    )
    
    #return redirect(f'/products/{slug}') we don't use it because we use ajax
        # get reviews 
    reviews = Review.objects.filter(product=product)
    page = render_to_string('include/reviews.html',{'reviews':reviews})
    return JsonResponse({'result':page})