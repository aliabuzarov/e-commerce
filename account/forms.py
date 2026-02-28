from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class SignInForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
                'class':'cs-form_field cs-accent_7_bg_2 cs-accent_10_border_2 cs-primary_color',
                'placeholder': 'Email'
            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class':'cs-form_field cs-accent_7_bg_2 cs-accent_10_border_2 cs-primary_color',
                'placeholder' : 'Password'}))


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'cs-form_field cs-accent_7_bg_2 cs-accent_10_border_2 cs-primary_color',
                'placeholder': 'Your Name'
            }),
            'email':forms.EmailInput(attrs={
                'class':'cs-form_field cs-accent_7_bg_2 cs-accent_10_border_2 cs-primary_color',
                'placeholder' : 'Email'

            }),
            'password' : forms.PasswordInput(attrs={
                'class':'cs-form_field cs-accent_7_bg_2 cs-accent_10_border_2 cs-primary_color',
                'placeholder' : 'Password'
            })

        }
        # def save(self,commit = ...):
        #     user = super().save(commit)
        #     user.set_password(form.cleaned_data['password'])
        #     user.save()