from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    """
    Stores information about the site, including a title, content, and a featured image.
    
    Attributes:
        title (str): The title of the about section.
        updated_on (datetime): The date and time when the about section was last updated.
        content (str): The main content of the about section.
        featured_image (CloudinaryField): The featured image for the about section.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default="placeholder")

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request, including the name, email, and message of the requester.
    
    Attributes:
        name (str): The name of the requester.
        email (EmailField): The email address of the requester.
        message (str): The message from the requester.
        read (bool): Whether the request has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"