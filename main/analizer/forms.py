from .models import Market
from django.forms import ModelForm, TextInput, widgets


class MarketForm(ModelForm):
    class Meta:
        model = Market
        fields = ['description']

        widgets = {
            "name": TextInput(attrs={
                'class': 'search',
                'placeholder': 'search'
            })
        }


