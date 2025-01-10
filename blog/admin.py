from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the Post model.
    Attributes:
        list_display (tuple): Fields to display in the list view.
        search_fields (list): Fields to include in the search functionality.
        list_filter (tuple): Fields to filter the list view.
        prepopulated_fields (dict): Fields to auto-populate based on other fields.
        summernote_fields (tuple): Fields to use the Summernote editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)