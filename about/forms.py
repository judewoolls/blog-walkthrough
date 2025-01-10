from .models import CollaborateRequest
from django import forms

class CollaborateForm(forms.ModelForm):
    """
    A form for submitting collaboration requests.
    This form allows users to input their name, email, and a message
    to request collaboration.
    Attributes:
        Meta:
            model (CollaborateRequest): The model associated with this form.
            fields (tuple): The fields to be included in the form.
    """

    class Meta:
        model = CollaborateRequest
        fields = ('name','email','message',)