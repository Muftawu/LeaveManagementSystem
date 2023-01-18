from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .authentication_backend import AuthenticationBackend
from django.contrib import messages
from .forms import * 

def loginpage(request):
    if request.user.is_authenticated:
        if request.user.user_type == '1':
            return redirect(reverse('supervisorDashboard'))
        else:
            return redirect(reverse('staffDashboard'))
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = AuthenticationBackend.authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            if request.user.user_type == '1':
                return redirect(reverse('supervisorDashboard'))
            else:
                return redirect(reverse('staffDashboard'))
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')

    context = {}
    return render(request, 'login.html', context)


def registerpage(request):
    userform = CustomUserForm()
    staff_form = StaffForm()

    if request.method == "POST":
        userform = CustomUserForm(request.POST)
        staff_form = StaffForm(request.POST, request.FILES)

        if userform.is_valid() and staff_form.is_valid():
            user = userform.save(commit=False)
            staff = staff_form.save(commit=False)
            staff.user = user
            
            user.save()
            staff.save()
            messages.success(request, 'Account creation success. You can now login')
            return redirect(reverse('login'))

    context = {'userform': userform, 'staff_form': staff_form}
    return render(request, 'register.html', context)


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'Thanks for visiting.')
    return redirect(reverse('login'))