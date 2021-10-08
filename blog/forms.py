from django import forms

from .models import Comment


class Leave_comment(forms.Form):

    class Meta:
        model = Comment
        fields = ['username', 'text']


class Feedback(forms.Form):
    email = forms.EmailField(required=True)
    feedback_message = forms.CharField(required=True)
