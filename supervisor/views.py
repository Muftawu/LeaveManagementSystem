from django.shortcuts import render
from leave.models import Leave, Staff


def supervisorDashboard(request):
    leaves = Leave.objects.all()
    staffs = Staff.objects.all()
    pending_leaves = leaves.filter(status=False)
    approved_leaves = leaves.filter(status=True)
    leave_total = leaves.count()
    staff_total = staffs.count()
    context = {
        'leaves': leaves, 
        'staffs': staffs,
        'leave_total': leave_total,
        'staff_total': staff_total,
        'approved_leaves': approved_leaves,
        'pending_leaves': pending_leaves,
        'approved_leaves_count': approved_leaves.count(),
        'pending_leaves_count': pending_leaves.count(),
        }
    return render(request, 'supervisorDashboard.html', context)