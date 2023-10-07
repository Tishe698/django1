from django import forms
from .models import Image

class ImageAdminForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    image2 = forms.ImageField(label='Image 2', required=False, widget=forms.FileInput)