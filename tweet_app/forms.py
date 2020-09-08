from django import forms
from django.forms import Textarea
from tweet_app.models import Tweet


class MakeTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["tweet"]
        widgets = {
            'tweet': Textarea(attrs={'onkeyup':"countChar(this)"})
        }