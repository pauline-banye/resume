from django import forms
# from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=234, required=True)
    message = forms.CharField(widget = forms.Textarea, required=True, max_length=5000)
