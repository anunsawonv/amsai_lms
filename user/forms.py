from django import forms
from django_recaptcha.fields import ReCaptchaField


class MyForm(forms.Form):
    captcha = ReCaptchaField()