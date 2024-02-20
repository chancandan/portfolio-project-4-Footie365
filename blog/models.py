from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Choices for post status (Draft or Published)
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
     # Title of the post
    title = models.CharField(max_length=200, unique=True)

    # Slug for the post URL
    slug = models.SlugField(max_length=200, unique=True)

    # Author of the post (linked to Django User model)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    # Last updated timestamp
    updated_on = models.DateTimeField(auto_now=True)

    # Content of the post
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # Method to get the number of likes for the post
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    # Post to which the comment is associated
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # Approval status of the comment
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


