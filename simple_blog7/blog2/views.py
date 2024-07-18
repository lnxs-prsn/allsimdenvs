# missing usersign up and login views and forms 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts} ) 

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form} )


@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, pk=slug)
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST'
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_derail', slug=post.pk)
    return render(request, 'blog/post_detail.html' {'post': post, 'comments': comments, 'comment_form': comment_form} )


@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, pk=slug)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', slug=post.pk)
        else:
            form = PostForm(instance=post)
    else return redirect('post_list')
    return render(request, 'blog/post_update.html', {'form': form, 'post': post} )

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, pk=slug)
    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
    else:
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'posft': post} )
