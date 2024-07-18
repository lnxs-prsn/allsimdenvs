from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('define_later')
    else:
        from = PostForm()
    return render(request, 'sim_blog6/post_form.html', {'form':form})


def comment_create(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id # assumes that post_id is passed as url parameter
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm(initial={'post': post_id})
    return render(request, 'sim_blog6/comment_form.html', {'form': form})


def post_list(request):
    if posts = Post.objects.all()
    return render(request, 'sim_blog6/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'sim_blog6/post_detail.html', {'post':post})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Post.Form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm(instance=post)
    return render(request, 'sim_blog6/post_form.html', {'form':form})



def 


# Create your views here.
