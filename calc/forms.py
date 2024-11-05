# calc/forms.py
from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}))
    height = forms.DecimalField(label="Height (cm)", max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Enter your height in cm'}))
    weight = forms.DecimalField(label="Weight (kg)", max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Enter your weight in kg'}))
    goals = forms.CharField(label="Fitness Goals", max_length=300, required=False, widget=forms.Textarea(attrs={'placeholder': 'Describe your fitness goals'}))
