from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.http import HttpResponse
from . import forms
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def postList(request):
    post_list = Post.objects.filter(postCreatedDate__lte = timezone.now()).order_by('-postCreatedDate')
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)


def postDetail(request, post_id):
    # retrieving post object from database using its primary key
    post = get_object_or_404(Post, pk = post_id)
    # sending that post object as a parameter to template in python dictionary structure
    return render (request, 'blog/post_detail.html', {'post': post})

def newPost(request):
    # getting PostForm
    form = PostForm(request.POST)
    # sending postForm as a parameter to template in python dictionary structure
    return render (request, 'blog/post_form.html', {'form': form})

# creates a blog post for drafts but not publish yet
def publishPost(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            # printing the post fields
            print ("title: " + form.cleaned_data['title'])
            print ("category: " + form.cleaned_data['category'])
            print ("content: " + form.cleaned_data['postContent'])
            # saving form data to our model
            form.save()
    return HttpResponseRedirect('/')


def editPost(request, post_id):
    # retrieving post object from database using its primary key
    post = get_object_or_404(Post, pk = post_id)
    # sending post object to display them in the form field
    form = PostForm(instance = post)
    # sending that form as a parameter to template
    return render (request, 'blog/post_edit.html', {'form': form})

def updatingEditedPost(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        form = forms.PostForm(request.POST, instance=post)

        if form.is_valid():
            # printing the post fields
            print ("title: " + form.cleaned_data['title'])
            print ("category: " + form.cleaned_data['category'])
            print ("content: " + form.cleaned_data['postContent'])
            # saving form data to our model
            form.save()
    # returning to homepage
    return HttpResponseRedirect('/')
