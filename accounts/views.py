from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm, ActivateForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from products.models import Product , Brand , Review
from orders.models import Order

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit=False) #create User -----> Create Profile
            user.is_active = False
            form.save()
            
            #email code
            profile = Profile.objects.get(user__username=username)
            profile.code
            
            #send email
            send_mail(
                "Activate your account",
                f" Welcome {username} \n Use this code {profile.code} to activate your account \nMystro team ",
                'rafah.hawa@yahoo.fr', #this will send the email
                [email],# this is where the email is going
                fail_silently=False,
            )
            return redirect(f'/accounts/{username/activate}')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})

#signup --------> code:email -----> activate:code ----> login (activated)

def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    
    if request.method == 'POST':
        form = ActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code :
                profile.code = ''
                profile.save()
                
                user = User.objects.get(username=username)
                user.is_active = True
                user.save()
                return redirect('/accounts/login')
        
    else:  # get
        form = ActivateForm()
        
    return render(request,'registration/activate.html',{'form':form})


def dashboard(request):
    # products 
    new_products = Product.objects.filter(flag='New').count()
    sale_products = Product.objects.filter(flag='Sale').count()
    feature_products = Product.objects.filter(flag='Feature').count()
    
    # all
    users = User.objects.all().count()
    products = Product.objects.all().count()
    orders = Order.objects.all().count()
    reviews = Review.objects.all().count()
    brands = Brand.objects.all().count()
    
    
    
    return render(request,'accounts/dashboard.html',{
        'new_products': new_products,
        'sale_products': sale_products , 
        'feature_products': feature_products,
        
        'users': users , 
        'products' : products , 
        'orders': orders , 
        'reviews' : reviews , 
        'brands': brands
    })