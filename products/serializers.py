from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages
from django.db.models.aggregates import Avg

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'
        
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    avg_rate2 = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_review_count(self,object):
        review_count = object.product_review.all().count()
        return review_count
    
    def get_avg_rate (self,object):
        total = 0
        reviews = object.product_review.all()
        for r in reviews :
            total+=r.rate
            
        if len(reviews) > 0:
            return round(total/len(reviews),2)
        else:
            return 0
    
    def get_avg_rate2(self,object):
        avg=object.product_review.aggregate(rate_avg=Avg('rate'))
        return round(avg['rate_avg'],2) if avg['rate_avg'] else 0
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    avg_rate2 = serializers.SerializerMethodField()
    images = ProductImagesSerializer(many=True, source='product_images')
    product_review = ProductReviewSerializer(many=True)
    
    class Meta:
        model = Product
        fields = '__all__'   
    def get_review_count(self,object):
        review_count = object.product_review.all().count()
        return review_count
    
    def get_avg_rate (self,object):
        total = 0
        reviews = object.product_review.all()
        for r in reviews :
            total+=r.rate
            
        if len(reviews) > 0:
            return round(total/len(reviews),2)
        else:
            return 0
    
    def get_avg_rate2(self,object):
        avg=object.product_review.aggregate(rate_avg=Avg('rate'))
        return round(avg['rate_avg'],2) if avg['rate_avg'] else 0
      
        
        
        
class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandDetailSerializer(serializers.ModelSerializer):
    product_brand = ProductListSerializer(many=True)
    class Meta:
        model = Brand
        fields = '__all__'
