from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Book, Review, UserProfile
from .forms import ReviewForm, UserProfileForm, UserRegistrationForm, UserLoginForm
from django.contrib import messages


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})



def book_detail(request, isbn):
    book = get_object_or_404(Book, isbn_number=isbn)
    reviews = book.reviews.all()
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})



@login_required
def add_review(request, isbn):
    book = get_object_or_404(Book, isbn_number=isbn)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', isbn=isbn)

    else:
        form = ReviewForm()
    return render(request, 'books/add_review.html', {'form': form, 'book': book})



@login_required
def user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'users/user_profile.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login_user.html', {'form': form})


def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def edit_book(request, isbn):
    book = get_object_or_404(Book, isbn_number=isbn)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', isbn=isbn)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, isbn):
    book = get_object_or_404(Book, isbn_number)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/confirm_delete.html', {'book': book})