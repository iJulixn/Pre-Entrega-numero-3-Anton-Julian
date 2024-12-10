from django import forms
from .models import motorv8,motori4,motorv6

class MotorV8Form(forms.ModelForm):
    class Meta:
        model = motorv8
        fields = ['cilindrada', 'marca', 'año', 'potencia']
class MotorV6Form(forms.ModelForm):
    class Meta:
        model = motorv6
        fields = ['cilindrada', 'marca', 'año', 'potencia']
class MotorI4Form(forms.ModelForm):
    class Meta:
        model = motori4
        fields = ['cilindrada', 'marca', 'año', 'potencia']