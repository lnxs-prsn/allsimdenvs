from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm, CommentForm


def index(request):
    post = Post.object.all().order_by('-created_at')
    categories = Category.object.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'index.html', context)

def post_detail(request, pk):
    post = Post.object.get(pk=pk)
    comments = post.comment_set.all().order_by('-created_at')
    comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment = comment_form.save(commit=False)
            post = comment.post
            comment.save()
            return redirect('post_detail', pk=pk)
    return render(request, 'post_detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'create_post.html', context)

# needs more views but ai did not provide at this time next time i know to ask for them


