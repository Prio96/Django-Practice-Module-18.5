from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,"Logged In Successfully")
                login(request,user)
                return redirect("Profile")
        else:
            messages.warning(request,"User Credentials are incorrect")
    else:
        form=AuthenticationForm()
    return render(request,'register.html',{'form':form,'type':'Login'})
        
        
@login_required
def Logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("Login")

def SignUp(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created Successfully")
            print(form.cleaned_data)
            form.save()
            return redirect("Login")
    else:
        form=SignupForm()
    return render(request,'register.html',{'form':form,'type':'Register'})

@login_required    
def Profile(request):
    return render(request,'profile.html',{'user':request.user,'type':'Profile'})

@login_required
def ChangePass(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            messages.success(request,"Password Changed Successfully")
            update_session_auth_hash(request,request.user)
            form.save()
            print(form.cleaned_data)
            return redirect("Login")
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form,'type':'Change Your Password'})
            
    
@login_required
def ChangePassWOOldPass(request):
    if request.method=='POST':
        form=SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            messages.success(request,"Password Changed Successfully")
            update_session_auth_hash(request,request.user)
            form.save()
            print(form.cleaned_data)
            return redirect("Login")
    else:
        form=SetPasswordForm(request.user)
    return render(request,'pass_change.html',{'form':form,'type':'Change Your Password'})

