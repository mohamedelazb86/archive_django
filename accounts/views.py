from django.shortcuts import render,redirect
from .forms import SignForm,ActivateForm
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    '''
    - create new user
    - stop activate this user
    - send email to this user
    - redirect activate html
    '''
    if request.method=='POST':
        form=SignForm(request.POST)
        if form.is_valid:
            myform=form.save(commit=False)
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']

            myform.save() # trigger create profile
            profile=Profile.objects.get(user__username=username)
            # send email to this user

            send_mail(
            "Activate Code",
            f"Welcome mr {username} \n pls use this code {profile.code}",
            "r_mido99@yahoo.com",
            [email],
            fail_silently=False,
                    )
            return redirect(f'/accounts/{username}/activate')
            


    else:
        form=SignForm()

   
    return render(request,'accounts/signup.html',{'form':form})

def activate_code(request,username):
    '''
    get your code
    check your code if = code.user
    active this user
    retun redirect login
    '''
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code==profile.code:
                profile.code=''

                user=User.objects.get(username=username)
                user.is_active=True
                user.is_staff=True
                user.save()
                profile.save()

                return redirect('/accounts/login')

    else:
        form=ActivateForm()
   
    return render(request,'accounts/activate_code.html',{'form':form})