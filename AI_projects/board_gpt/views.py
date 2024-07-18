from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, Commentform

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list,html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_by = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'post_detail.html', {'post': post, 'form': form})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'post_create.html', {'form': form})