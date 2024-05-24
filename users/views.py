from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from django.contrib import messages  # type: ignore
from .form import UserRegisterForm 

# Create your views here.
def register(request):
    if request.method =='POST':
        form=UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request, f'Account is created for {username}!Now,you can login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


