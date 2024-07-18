from django import forms
from .models import Post, Comment

class PostForm(form.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentfields = ['author', 'content']

        