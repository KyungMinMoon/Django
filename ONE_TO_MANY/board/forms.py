from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    #validation

    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', )