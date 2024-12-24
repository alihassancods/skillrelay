from django import forms
from .models import FreelancerProfile, EmployerProfile

class FreelancerProfileForm(forms.ModelForm):
    class Meta:
        model = FreelancerProfile
        fields = ['profile_picture', 'description', 'display_name', 'username']

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['image', 'display_name', 'country']
