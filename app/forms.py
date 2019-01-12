from django import forms
from .models  import Barreau, Plate

class BarreauForm(forms.ModelForm):
    class Meta:
        model = Barreau
        fields = ('a', 'b', 'l', 'csvfile')


    # a = forms.FloatField(label='dimension-a-barreau', localize=True)
    # b = forms.FloatField(label='dimension-b-barreau', localize=True)
    # l = forms.FloatField(label='dimension-l-barreau', localize=True)
    #
    # csvfile = forms.FileField()
    # a = forms.FloatField()
    # b = forms.FloatField()
    # l = forms.FloatField()

class PlateForm(forms.ModelForm):
    class Meta:
        model = Plate
        fields = ('a', 'b', 'l', 'csvfile')
