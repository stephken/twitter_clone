from django  import forms 
from twitter_user_app.models import TwitterUser


class SignupForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)