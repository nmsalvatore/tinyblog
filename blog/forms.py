from django.forms import ModelForm
from django import forms
from blog.models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'title': ''}
        widgets = {'title': forms.TextInput(attrs={"placeholder": "Title"})}
