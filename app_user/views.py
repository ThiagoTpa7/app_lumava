from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_user.models import Users
from django.contrib.auth import authenticate, login as auth_login, logout


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password= password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')
    
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html')
        else:
            if password == password2:
                usuario = User.objects.create_user(username=username, password=password, email=email)
                usuario.save()
                auth_login(request,usuario)
                return render(request, 'home.html')
            else:
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')
    
def user_logout(request):
    logout(request)
    return render(request, 'home.html')

