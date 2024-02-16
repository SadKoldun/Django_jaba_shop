from django import forms

from goods.models import Comment


class CommentForm(forms.Form):
    comment_text = forms.CharField(required=True)


