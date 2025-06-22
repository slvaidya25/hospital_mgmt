from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'dob': forms.DateInput(attrs={'placeholder': 'DoB YYYY-MM-DD'}),
            #'blood_group': forms.TextInput(attrs={'placeholder': 'Blood Group'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'address': forms.Textarea(attrs={'placeholder': 'Address', 'rows': 2, 'cols': 80}),
            'emergency_contact': forms.TextInput(attrs={'placeholder': 'Emergency Contact'}),
        }
