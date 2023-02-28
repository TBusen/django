from django import forms
from .models import Review

from django.forms import ModelForm
# this is a comment

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name',max_length=100,)
#     last_name = forms.CharField(label="Last Name",max_length=100)
#     email = forms.EmailField(label='Email')
#     # review = forms.CharField(label='Please write your feedback here')
#     # WIDGETS
#     # review = forms.CharField(widget=forms.Textarea())

#     review = forms.CharField(widget=forms.Textarea(attrs={'class':'myform'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review 
        # fields = ['first_name','last_name','stars']
        fields = "__all__"

        labels = {
            'first_name':"First Name",
            'last_name':"Last Name",
            'stars':'Rating'
        }
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes
        error_messages = {
            'stars':{
                'min_value':"Yo! Minimum value must be 1",
                'max_value':"Yo! Max value is 5"
            }
        }