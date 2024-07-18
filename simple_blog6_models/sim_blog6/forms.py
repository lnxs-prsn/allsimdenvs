django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['text', 'author', 'post']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.HiddenInput(),

        }