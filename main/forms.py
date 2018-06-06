from django import forms
from django.core import validators

class FormName (forms.Form):
    BHK = forms.IntegerField()
    FSI = forms.IntegerField()
    CHOICES=[('Naboo','Naboo'),('Alderaan','Alderaan'),('Endor','Endor'),('Tatooine','Tatooine'),('Hoth','Hoth')]

    Planet = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    botcatcher= forms.CharField(required=False,widget=forms.HiddenInput)
