from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comment


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'conten']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']