from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

from .models import Blog, BlogPost
from .forms import BlogPostForm


def post_list_view(request, path):
    active_path = request.session.get("active_path", None)
    if active_path != path:
        request.session['active_path'] = path

    blog = Blog.objects.get(path=path)
    blogs = Blog.objects.all()
    posts = blog.posts.all()
    context = {"blogs": blogs, "blog": blog, "posts": posts}
    return render(request, "blog/post_list.html", context)


def post_detail_view(request, path, slug):
    active_path = request.session.get("active_path", None)
    if active_path != path:
        request.session['active_path'] = path

    blog = Blog.objects.get(path=path)
    blogs = Blog.objects.all()
    post = BlogPost.objects.get(slug=slug)
    context = {"blogs": blogs, "blog": blog, "post": post}
    return render(request, "blog/post_detail.html", context)


@login_required
def post_new_view(request, path):
    blog = Blog.objects.get(path=path)

    if request.user != blog.author:
        raise PermissionDenied

    else:
        active_path = request.session.get("active_path", None)
        if active_path != path:
            request.session['active_path'] = path

        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.blog = blog
                post.author = request.user
                post.body = request.POST.get('content')
                post.slug = slugify(post.title)
                post.is_published = True
                post.save()
            return redirect("post_list", path=path)

        else:
            blogs = Blog.objects.all()
            form = BlogPostForm()
            context = {"blogs": blogs, "blog": blog, "form": form}
            return render(request, "blog/post_new.html", context)


@login_required
def post_edit_view(request, slug, path):
    blog = Blog.objects.get(path=path)
    post = BlogPost.objects.get(slug=slug)

    if request.user != blog.author:
        raise PermissionDenied

    else:
        active_path = request.session.get("active_path", None)
        if active_path != path:
            request.session['active_path'] = path

        if request.method == 'POST':
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                updated_post = form.save(commit=False)
                updated_post.blog = blog
                updated_post.author = request.user
                updated_post.body = request.POST.get('content')
                updated_post.slug = slugify(updated_post.title)
                updated_post.save()
            return redirect("post_detail", path=blog.path, slug=slug)

        else:
            blogs = Blog.objects.all()
            form = BlogPostForm(instance=post)
            context = {"blogs": blogs, "blog": blog, "post": post, "form": form}
            return render(request, "blog/post_edit.html", context)


@login_required
def post_delete_view(request, slug, path):
    post = BlogPost.objects.get(slug=slug)

    if post.author != request.user:
        raise PermissionDenied
    else:
        post.delete()
        return redirect("post_list", path=path)
