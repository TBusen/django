from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):

#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label = 'Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please Write your Review here', widget=forms.Textarea(attrs={'class':'myform',


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ["first_name", "last_name", "stars"]
        # pass in all fields
        fields = "__all__"

        labels = {
            "first_name": "YOUR FIRST NAME",
            "last_name": "Last Name",
            "stars": "Rating",
        }
        # optional custom error messages
        error_messages = {
            "stars": {
                "min_value": "Yo min value is 1",
                "max_value": "yo max value is 5",
            }
        }
