"""
from django.forms import ModelForm
from .models import cards

class CreateCardForm(ModelForm):
    class Meta:
        model = cards
        fields = ['title', 'content', 'tag', 'url_l']
"""