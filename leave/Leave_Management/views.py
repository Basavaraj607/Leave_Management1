from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from .models import LeaveApplication, LeaveBalance
from .forms import LeaveApplyForm, CustomUserCreationForm
from .utils import manager_required, days_between


@login_required
def dashboard(request):
    profile = getattr(request.user, 'profile', None)

    if profile and profile.role == 'MGR':
        team = User.objects.filter(profile__manager=request.user)
        pending = LeaveApplication.objects.filter(user__in=team, status='PEN').order_by('start_date')

        calendar = {}
        for leave in LeaveApplication.objects.filter(user__in=team).order_by('start_date'):
            key = leave.start_date.isoformat()
            calendar.setdefault(key, []).append(leave)

        context = {
            'is_manager': True,
            'team': team,
            'pending': pending,
            'calendar': calendar,
        }
        return render(request, 'leaves/manager_dashboard.html', context)

    balance, _ = LeaveBalance.objects.get_or_create(user=request.user)
    my_leaves = LeaveApplication.objects.filter(user=request.user).order_by('-applied_at')
    pending = my_leaves.filter(status='PEN')
    context = {
        'is_manager': False,
        'balance': balance,
        'my_leaves': my_leaves,
        'pending': pending,
    }
    return render(request, 'leaves/employee_dashboard.html', context)


@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveApplyForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.status = 'PEN'
            leave.save()
            messages.success(request, "Leave applied successfully.")
            return redirect('dashboard')
    else:
        form = LeaveApplyForm()
    return render(request, 'leaves/apply_leave.html', {'form': form})


@login_required
def cancel_leave(request, pk):
    leave = get_object_or_404(LeaveApplication, pk=pk, user=request.user)
    if leave.status == 'PEN':
        leave.status = 'CAN'
        leave.save()
        messages.success(request, "Leave cancelled.")
    else:
        messages.error(request, "Cannot cancel non-pending leave.")
    return redirect('dashboard')


@login_required
@manager_required
def approve_leave(request, pk):
    leave = get_object_or_404(LeaveApplication, pk=pk)
    if not getattr(leave.user, 'profile', None) or leave.user.profile.manager != request.user:
        messages.error(request, "You are not authorized to act on this leave.")
        return redirect('dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')
        manager_comments = request.POST.get('manager_comments', '').strip()
        if action == 'approve':
            leave.status = 'APP'
            leave.manager_comments = manager_comments
            leave.updated_at = timezone.now()
            leave.save()

            days = days_between(leave.start_date, leave.end_date)
            lb, _ = LeaveBalance.objects.get_or_create(user=leave.user)
            if leave.leave_type == 'CAS':
                lb.casual = max(lb.casual - days, 0)
            elif leave.leave_type == 'SIC':
                lb.sick = max(lb.sick - days, 0)
            elif leave.leave_type == 'EAR':
                lb.earned = max(lb.earned - days, 0)
            lb.save()

            messages.success(request, f"Leave approved and {days} day(s) deducted from {leave.user.username}'s balance.")
        elif action == 'reject':
            leave.status = 'REJ'
            leave.manager_comments = manager_comments
            leave.updated_at = timezone.now()
            leave.save()
            messages.success(request, "Leave rejected.")
        else:
            messages.error(request, "Unknown action.")
        return redirect('dashboard')

    return render(request, 'leaves/approve_leave.html', {'leave': leave})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, "Account created successfully — you can now login.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
