from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    """
    View to list all published blog posts.
    
    Attributes:
        queryset (QuerySet): The queryset of published posts.
        template_name (str): The template to render the post list.
        paginate_by (int): The number of posts to display per page.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    View to display the details of a single blog post, including its comments.
    
    Args:
        request (HttpRequest): The request object.
        slug (str): The slug of the post to display.
    
    Returns:
        HttpResponse: The rendered post detail page.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            ) 

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )

def comment_edit(request, slug, comment_id):
    """
    View to edit an existing comment.
    
    Args:
        request (HttpRequest): The request object.
        slug (str): The slug of the post to which the comment belongs.
        comment_id (int): The ID of the comment to edit.
    
    Returns:
        HttpResponseRedirect: Redirects to the post detail page.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete an existing comment.
    
    Args:
        request (HttpRequest): The request object.
        slug (str): The slug of the post to which the comment belongs.
        comment_id (int): The ID of the comment to delete.
    
    Returns:
        HttpResponseRedirect: Redirects to the post detail page.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))