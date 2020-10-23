from django import forms

class LoginForm(forms.Form):
    #max_length matches max_length for username field in pages/models.TIUser
    username = forms.CharField(label="username", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
