from . import models as M
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = M.Post
        fields = '__all__'
        widgets = {'date_posted': DateInput()}

class UpdatePostForm(forms.ModelForm):

    class Meta:
        model = M.Post
        fields = ['title', 'content', 'date_posted']
        widgets = {'date_posted': DateInput()}

