from django import forms
from .models import Comment, Post, Category


# Form for adding comments to a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Form for creating and updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'category', 'content', 'featured_image', 'excerpt', 'status']
