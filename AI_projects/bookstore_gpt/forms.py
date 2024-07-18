from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Review, UserProfile, Book

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class ReviewForm(forms.ModelForm):
    class Meta:
        codel = Review
        fields = ['text', 'rating']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'favorite_books']
        widgets = {
            'favorite_books': forms.CheckboxSelectMultiple(),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 'stock', 'cover_image', 'publish_date', 'isbn_number', 'genre']