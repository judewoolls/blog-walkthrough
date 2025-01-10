from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    Stores a single blog post entry, related to :model:`auth.User`.
    
    Attributes:
        title (str): The title of the post.
        slug (str): The slug for the post URL.
        author (User): The author of the post.
        featured_image (CloudinaryField): The featured image for the post.
        content (str): The main content of the post.
        created_on (datetime): The date and time when the post was created.
        status (int): The publication status of the post.
        excerpt (str): A short excerpt from the post.
        updated_on (datetime): The date and time when the post was last updated.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment, related to :model:`blog.Post` and :model:`auth.User`.
    
    Attributes:
        post (Post): The post that the comment is related to.
        author (User): The author of the comment.
        body (str): The main content of the comment.
        approved (bool): Whether the comment is approved for display.
        created_on (datetime): The date and time when the comment was created.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment: {self.body} by {self.author}"