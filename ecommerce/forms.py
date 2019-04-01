from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Your Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Your Email"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "id": "content", "placeholder": "Your Content"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email has to be gmail.com  ")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)