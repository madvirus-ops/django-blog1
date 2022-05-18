from django import forms
from .models import Posts


class Postsform(forms.Form):

    class Meta:
        model = Posts 
        fields = ["title","content","image"]