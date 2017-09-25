from django import forms
from .models import Picture, List

class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = "__all__"


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = "__all__"
        widgets = {
            'imgs': forms.CheckboxSelectMultiple()
        }
