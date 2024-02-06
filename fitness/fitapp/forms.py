from django import forms
from captcha.fields import ReCaptchaField

class MyForm(forms.Form):
    # Define your form fields
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'margin: 10px; padding: 5px; border: none; background-color: rgba(156, 77, 156, 0.3); border-radius: 10px; font-weight: bold; font-size: small; font-family: "Montserrat", sans-serif; color: #aa38a4;'
            }
        )
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'style': 'margin: 10px; padding: 5px; border: none; background-color: rgba(156, 77, 156, 0.3); border-radius: 10px; font-weight: bold; font-size: small; font-family: "Montserrat", sans-serif; color: #aa38a4;'
            }
        )
    )

    # Add the reCAPTCHA field
    captcha = ReCaptchaField()

