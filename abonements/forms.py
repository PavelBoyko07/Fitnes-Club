from django import forms
from .models import Review, ContactMessage

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Расскажите о вашем опыте...'}),
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=[(i, f'{i} ★') for i in range(1, 6)]),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваше сообщение'}))