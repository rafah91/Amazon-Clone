from django.shortcuts import render , redirect
from .models import Cart , CartDetail , Order, Coupon , OrderDetail
from products.models import Product
from settings.models import DeliveryFee
import datetime
import stripe
from django.http import JsonResponse
from django.conf import settings
from utils.generate_code import generate_code


def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'orders/orderlist.html',{'orders':orders})


def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail,created = CartDetail.objects.get_or_create(cart=cart , product=product)
    
    cart_detail.quantity = quantity
    cart_detail.total = round(quantity * product.price,2)
    cart_detail.save()
    
    return redirect(f"/products/{product.slug}")

def checkout(request):
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    sub_total = cart.cart_total()
    
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    
    if request.method == 'POST':
        code = request.POST['coupon_code']
        coupon = Coupon.objects.get(code=code)
        
        if coupon and coupon.quantity > 0 :
            today = datetime.datetime.today().date()
            if today >= coupon.start_date and today < coupon.end_date : 
                coupon_value = sub_total / 100*coupon.discount
                sub_total = sub_total - coupon_value
                total = sub_total + delivery_fee
                
                cart.coupon = coupon
                cart.cart_total_discount = sub_total
                cart.save()
            
                return render(request,'orders/checkout.html',{
                        'cart_detail': cart_detail , 
                        'delivery_fee': delivery_fee , 
                        'sub_total': sub_total , 
                        'discount': coupon_value , 
                        'total': total , 
                        'pub_key':pub_key
                        
                    })
    
    
    discount = 0
    total = sub_total + delivery_fee
    
    
    
    return render(request,'orders/checkout.html',{
        'cart_detail': cart_detail , 
        'delivery_fee': delivery_fee , 
        'sub_total': sub_total , 
        'discount': discount , 
        'total': total , 
        'pub_key':pub_key
    })
    
    
    
    return render(request,'orders/checkout.html',{})


# create invoice link 
def process_payment(request):  
    
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    delivery_fee = DeliveryFee.objects.last().fee
    
    if cart.cart_total_discount:
        total = cart.cart_total_discount + delivery_fee
        
    else:
        total = cart.cart_total() + delivery_fee
     
     
    code = generate_code() 
    
    # store code in django session 
    request.session['order_code'] = code
    request.session.save()
     
    stripe.api_key = settings.STRIPE_API_KEY_SECRET 
    checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data' : {
                            'currency' : 'usd' , 
                            'product_data' : { 'name' : code} , 
                            'unit_amount' : int(total*100)
                        },
                        'quantity':1
                        },
                ],
                mode='payment',
                success_url= 'http://127.0.0.1:8000/orders/checkout/payment/success',
                cancel_url= 'http://127.0.0.1:8000/orders/checkout/payment/failed',
            )


    return JsonResponse({'session': checkout_session})

#success
def payment_success(request):
    cart = Cart.objects.get(user=request.user , status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    
    # get order code from session 
    order_code = request.session.get('order_code')
    
    # new order  : cart
    new_order = Order.objects.create(
        user = request.user , 
        code = order_code , 
        coupon = cart.coupon , 
        order_total_discount = cart.cart_total_discount
    )

    # order_detail : cart_detail
    for object in cart_detail:
        OrderDetail.objects.create(
            order = new_order , 
            product = object.product , 
            quantity = object.quantity , 
            price = object.product.price , 
            total = object.quantity * object.product.price
        ) 
        
    cart.status = 'Completed'
    cart.save()
    

    return render(request,'orders/success.html',{'code':order_code})

#failed
def payment_failed(request):
    code=''
    return render(request,'orders/failed.html',{'code':code})
