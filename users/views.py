from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    
def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect ('home')
        # Redirect to a success page.
        ...
    else:
        messages.success(request,('The was an error logging,Try Again '))
        return redirect('login')
        # Return an 'invalid login' error message.
        
        ...

