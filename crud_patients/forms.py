from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("fname","lname","gender","age","disease","doctor","doctor_fees","start_med")
