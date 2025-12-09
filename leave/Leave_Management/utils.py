from django.contrib.auth.decorators import user_passes_test
from datetime import timedelta

def role_required(role):
    def check(user):
        return hasattr(user, 'profile') and user.profile.role == role
    return user_passes_test(check, login_url='login')

def manager_required(view_func):
    return role_required('MGR')(view_func)

def employee_required(view_func):
    return role_required('EMP')(view_func)

def days_between(start_date, end_date):
    if start_date and end_date:
        return (end_date - start_date).days + 1
    return 0
