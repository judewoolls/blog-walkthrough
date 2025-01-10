from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the About model.
    
    Attributes:
        summernote_fields (tuple): Fields to use with the Summernote editor.
    """
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin interface options for the CollaborateRequest model.
    
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """
    list_display = ('message', 'read',)