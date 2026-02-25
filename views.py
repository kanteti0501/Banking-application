from django.shortcuts import render
from .models import User_Accounts

# Create your views here.

def signup(request):

    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")
        print(email,password,confirm_password)

        if password != confirm_password:
            return render(request,'user_accounts/signup.html', {"error" : "Passwords are not identical"})

        User_Accounts.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            password=password
        )


        return render(request,'user_accounts/signup.html')
    return render(request,'user_accounts/signup.html')