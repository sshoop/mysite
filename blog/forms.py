from django import forms
from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_name', 'comment_text']

        widgets = {
            'comment_name': forms.TextInput(attrs={
                'size': 105,
                'class': 'form_control',
                'placeholder': '昵称',
                'aria-describedby': 'sizing-addonl',

            }),
            'comment_text': forms.TextInput(attrs={
                'size': 105,
                'class': 'special',
                'placeholder': '我来评论两句',
            }),
        }

