from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    ROLE_CHOICES = (
        ('EMP', 'Employee'),
        ('MGR', 'Manager'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='EMP')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='team_members')

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


class LeaveBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    casual = models.IntegerField(default=12)
    sick = models.IntegerField(default=8)
    earned = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} balance"


class LeaveApplication(models.Model):
    LEAVE_TYPE = (('CAS', 'Casual'), ('SIC', 'Sick'), ('EAR', 'Earned'))
    STATUS = (('PEN','Pending'),('APP','Approved'),('REJ','Rejected'),('CAN','Cancelled'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=3, choices=LEAVE_TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=3, choices=STATUS, default='PEN')
    manager_comments = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} {self.leave_type} {self.start_date}→{self.end_date}"
