from django.shortcuts import render
from .models import Blog, BlogPost

def post_list_view(request, path):
    blog = Blog.objects.get(path=path)
    blogs = Blog.objects.all()
    posts = blog.posts.all()
    context = {"blogs": blogs, "blog": blog, "posts": posts}
    return render(request, "blog/post_list.html", context)

def post_detail_view(request, path, slug):
    blog = Blog.objects.get(path=path)
    blogs = Blog.objects.all()
    post = BlogPost.objects.get(slug=slug)
    context = {"blogs": blogs, "blog": blog, "post": post}
    return render(request, "blog/post_detail.html", context)
