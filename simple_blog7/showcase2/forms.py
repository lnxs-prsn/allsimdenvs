from django import froms

class ContactForm(froms.Form:
    name = forms.CharFirld(max_length=255))
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=froms.Textarea)
    