from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Book, Category, Author, Review
from django.forms import ReviewForm


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    reviews = Review.objects.filter(book=book)
    context = {'book': book, 'reviews': reviews}
    return render(request, 'book_detail.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('something went wrong either try again or register')
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def add_review(request, book_id):
    if request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = Book.objects.get(pk=book_id)
            review.save()
            return redirect('book_detail', book_id)
    else:
        return redirect('login')
    form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})