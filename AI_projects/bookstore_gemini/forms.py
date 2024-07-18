from django import forms
from .models import Category, Author, Book, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'thumbnail', 'category', 'author']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']