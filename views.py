from .models import User
from django.shortcuts import render, redirect


# Create your views here.
def account_opening(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        print(username, password, first_name, last_name, email, phone, role)

        if User.objects.filter(username=request.user.username).exists():
            return render(request, 'users/error.html')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            role=role
        )

    return render(request,'users/account_opening.html')
