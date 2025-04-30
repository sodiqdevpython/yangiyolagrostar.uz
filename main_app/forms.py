from django import forms
from .models import Contact, Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabaringiz', 'rows': 6}),
        }
        labels = {
            'name': "",
            'phone_number': "",
            'text': ""
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Izohingiz', 'rows': 4}),
        }
        labels = {
            'name': '',
            'text': ''
        }