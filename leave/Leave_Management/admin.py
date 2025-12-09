from django.contrib import admin
from .models import Profile, LeaveBalance, LeaveApplication

admin.site.register(Profile)
admin.site.register(LeaveBalance)
admin.site.register(LeaveApplication)

