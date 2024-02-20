from .models import Comment
from django import forms
from .models import Post


# Form for adding comments to a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Form for creating and updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'featured_image', 'excerpt', 'status']



