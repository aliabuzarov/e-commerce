from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'message'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'cs-form_field cs-white_bg cs-accent_30_border_2 cs-primary_color',
                'placeholder': 'First Name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class': 'cs-form_field cs-white_bg cs-accent_30_border_2 cs-primary_color',
                'placeholder':'Last Name' 
            }),
            'phone' : forms.TextInput(attrs={

                'class':'cs-form_field cs-white_bg cs-accent_30_border_2 cs-primary_color',
                'placeholder':'Phone'
            }),
            'email': forms.EmailInput(attrs={
                'class':'cs-form_field cs-white_bg cs-accent_30_border_2 cs-primary_color',
                'placeholder': 'Email'

            }),
            'message': forms.Textarea(attrs={
                'class':'cs-form_field cs-white_bg cs-accent_30_border_2 cs-primary_color',
                'placeholder':'Message'
            })

        }
