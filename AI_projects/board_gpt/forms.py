from django import forms
from .models import Post, Comment

class PostForm(forms.ModelsForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

class Commentform(models.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']