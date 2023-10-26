
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, BrandSerializer
from rest_framework import filters
from .models import Product, Brand
from .mypagination import MyPagination



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['brand','flag']
    search_fields = ['name', 'description', 'subtitle']

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class=BrandSerializer
    pagination_class=MyPagination

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class=BrandSerializer