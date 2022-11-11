from django import forms

from .models import Card, Contact

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ('user', 'date_added')
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('user', 'card')