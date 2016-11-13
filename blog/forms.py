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
                'aria_describedby': 'sizing-addonl',

            }),
            'comment_text': forms.TextInput(attrs={
                'size': 105,
                'class': 'special',
                'placeholder': '我来评论两句',
            }),
        }


class SearchForm(forms.Form):
    search_name = forms.CharField(
        label='查询文章',
        max_length=50,
        error_messages={
            'required': '请输入文章名字',
            'min_length': u'不能少于5个字',
        },
        widget=forms.TextInput(
            attrs={
                'size': '40',
                'placeholder': 'search name',
                'class': 'form-control',
                'id': "inputPassword",
            }
        )
    )

