from django import forms
from .models import LeaveApplication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LeaveApplyForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['start_date', 'end_date', 'leave_type', 'reason']

    def clean(self):
        cleaned = super().clean()
        s = cleaned.get('start_date')
        e = cleaned.get('end_date')
        if s and e and e < s:
            raise forms.ValidationError("End date cannot be before start date.")
        return cleaned


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user
    