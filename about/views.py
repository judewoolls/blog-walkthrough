from django.shortcuts import render, get_object_or_404
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.

def AboutDisplay(request):
    """
    View to display the About page and handle collaboration form submissions.
    
    Args:
        request (HttpRequest): The request object.
    
    Returns:
        HttpResponse: The rendered About page with the About section content and collaboration form.
    """
    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavor to respond within 2 working days."
            )
    
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )