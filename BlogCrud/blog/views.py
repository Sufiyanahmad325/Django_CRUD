from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'blog/register.html')


        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, 'User created successfully!')
        return render(request, "blog/register.html")
    
    return render(request, 'blog/register.html')