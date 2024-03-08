from django import forms


class CommentForm(forms.Form):
    rating = forms.ChoiceField(choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ], )
    comment_text = forms.CharField(required=True)


