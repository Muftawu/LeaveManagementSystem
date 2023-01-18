from django.shortcuts import render, redirect, reverse
from . models import * 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import NewLeaveForm

@login_required(login_url='login/')
def staffDashboard(request):
    user = request.user 
    staff = user.staff
    leaves = Leave.objects.filter(staff=staff).all()
    context = {'leaves': leaves}
    return render(request, 'staffDashboard.html', context)


@login_required(login_url='login/')
def new_leave(request):
    user = request.user
    staff = user.staff

    form = NewLeaveForm()

    if request.method == "POST":
        form = NewLeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.staff = staff
            leave.save()
            return redirect(reverse('staffDashboard'))

    context = {'form': form}
    return render(request, 'new_leave.html', context)


@login_required(login_url='login/')
def view_leave(request, leave_id):
    user = request.user
    staff = user.staff 
    leave = Leave.objects.filter(staff=staff).get(id=leave_id)

    context = {'leave': leave}
    return render(request, 'view_leave.html', context)


@login_required(login_url='login/')
def approved_leaves(request):
    user = request.user
    staff = user.staff
    approved_leaves = Leave.objects.filter(staff=staff, status=True)
    context = {'approved_leaves': approved_leaves}
    return render(request, 'approved.html', context)

@login_required(login_url='login/')
def pending_leaves(request):
    user = request.user
    staff = user.staff
    pending_leaves = Leave.objects.filter(staff=staff, status=False)
    context = {'pending_leaves': pending_leaves}
    return render(request, 'pending.html', context)