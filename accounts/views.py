from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm
from django.core.mail import send_mail


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
    return render(request,'signup.html',{'form':form})

#signup --------> code:email -----> activate:code ----> login (activated)

def activate(request,username):
    pass