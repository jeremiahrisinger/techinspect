from django import forms
from django.forms import ModelForm
from pages.models import Image, TIUser, Waiver

class LoginForm(forms.Form):
    #max_length matches max_length for username field in pages/models.TIUser
    username = forms.CharField(label="username", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Verify Password'}))
    image = forms.ImageField(required=False)
    def verify_password(self):
        passw = self.cleaned_data['password']
        conf_pass = self.cleaned_data['confirm_pass']
        if passw != conf_pass:
            return False
        return True
    def create_user(self):
        if self.verify_password():
            entry = TIUser.objects.create_user(self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
            #user_image = Image(image=self.cleaned_data['image'])
            #user_image.save()
            #key = user_image.imageID
            #entry.image = user_image
            entry.save()
            return True and TIUser.objects.get(username=entry.username)# and Image.objects.get(pk=key)
        return False
         

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class WaiverForm(ModelForm):
    class Meta:
        model = Waiver
        fields = ['waiverDate', 'waiverName']
