django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_lenght=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


