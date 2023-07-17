from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs= {'class' : 'form-control'}))
    email = forms.EmailField(widget = forms.TextInput(attrs= {'class' : 'form-control'}))
    message = forms.CharField(widget = forms.Textarea(attrs= {'class' : 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Only gmail is approved")
        return email
