# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Post
from .forms import PostForm, CommentForm


def base_index(request):
    return render(request, 'base_index.html')


def list_posts(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # ultimas 4 entradas
    # 'post_list': Post.objects.all().order_by("-publish", "-created")[:4]
    posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': posts,})


def base_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'base_post.html', {'post': post})


@staff_member_required
def base_post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('base_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'base_post_add.html', {'form': form})


@staff_member_required
def base_post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('base_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'base_post_edit.html', {'form': form})


@login_required
def base_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('base_post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'base_comment.html', {'form': form})


"""
def base_auth_reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list_posts')
    else:
        form = UserCreationForm()
    return render(request, 'base_auth_reg.html', {'form': form})
"""