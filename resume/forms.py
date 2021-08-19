from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=234, required=True)
    message = forms.CharField(widget = forms.Textarea, max_length=5000)
    
    