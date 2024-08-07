from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Choices for post status (Draft or Published)
STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    # Title of the post
    title = models.CharField(max_length=200, unique=True)

    # Slug for the post URL
    slug = models.SlugField(max_length=200, unique=True)

    # Author of the post (linked to Django User model)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    # Category of the post (linked to Category model)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )

    # Last updated timestamp
    updated_on = models.DateTimeField(auto_now=True)

    # Content of the post
    content = models.TextField()

    # Featured image for the post
    featured_image = CloudinaryField('image', default='placeholder')

    # Short excerpt from the post
    excerpt = models.TextField(blank=True)

    # Created timestamp
    created_on = models.DateTimeField(auto_now_add=True)

    # Status of the post (Draft or Published)
    status = models.IntegerField(choices=STATUS, default=0)

    # Likes for the post (many-to-many relationship with User model)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # Method to get the number of likes for the post
    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    # Post to which the comment is associated
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    # Created timestamp
    created_on = models.DateTimeField(auto_now_add=True)

    # Approval status of the comment
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
