from django import forms
from .models import HeartPrediction

#create a form for prediction input
class HeartPredictionForm(forms.ModelForm):
    class Meta:
        model = HeartPrediction
        fields = [
            'age',
            'anemia',
            'creatinine_phosphokinase',
            'diabetes',
            'ejection_fraction',	
            'high_blood_pressure',
            'platelets',
            'serum_creatinin',	
            'serum_sodium',	
            'sex',
            'smoking',
            'time',
            ]
        widgets = {
            'age' : forms.NumberInput(attrs={'class': 'form-control'}),
            'anemia': forms.NumberInput(attrs={'class': 'form-control'}),
            'creatinine_phosphokinase': forms.NumberInput(attrs={'class': 'form-control'}),
            'diabetes': forms.NumberInput(attrs={'class': 'form-control'}),
            'ejection_fraction': forms.NumberInput(attrs={'class': 'form-control'}),	
            'high_blood_pressure' : forms.NumberInput(attrs={'class': 'form-control'}),
            'platelets' : forms.NumberInput(attrs={'class': 'form-control'}),
            'serum_creatinin': forms.NumberInput(attrs={'class': 'form-control'}),	
            'serum_sodium': forms.NumberInput(attrs={'class': 'form-control'}),	
            'sex': forms.NumberInput(attrs={'class': 'form-control'}),
            'smoking': forms.NumberInput(attrs={'class': 'form-control'}),
            'time': forms.NumberInput(attrs={'class': 'form-control'}),

        }