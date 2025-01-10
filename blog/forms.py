from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments.
    This form is based on the `Comment` model and includes only the `body` field.
    Attributes:
        Meta (class): A nested class that defines metadata for the form.
            model (Comment): The model that this form is based on.
            fields (tuple): A tuple specifying the fields to include in the form.
    """

    class Meta:
        model = Comment
        fields = ('body',)

