from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect, redirect
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

    # navigating to detail page
    return redirect('blog:postDetail', post_id = post.pk)

def deletePost(request, post_id):
    # deleting a record from Post model
    Post.objects.filter(pk = post_id).delete()
    return HttpResponseRedirect('/')

def likePost(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.postLikes += 1
    post.save()
    return redirect('blog:postDetail', post_id = post.pk)


def addComment(request, post_id):
    form = CommentForm(request.POST)
    return render (request, 'blog/comment_form.html', {'form': form})


def publishComment(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            print ("commentContent: " + form.cleaned_data['commentContent'])
            # getting the comment
            comment = form.save(commit=False)
            # specifying the post that comment belongs to
            comment.post = post
            form.save()

    return redirect('blog:postDetail', post_id = post.pk)


def editComment(request, post_id, comment_id):
        post = get_object_or_404(Post, pk = post_id)
        comment = get_object_or_404(Comment, pk = comment_id)
        # sending comment object to display them in the form field
        form = CommentForm(instance = comment)
        # sending that form as a parameter to template
        return render (request, 'blog/comment_edit.html', {'form': form})


def updateEditedComment(request, post_id, comment_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        comment = get_object_or_404(Comment, pk = comment_id)
        form = forms.CommentForm(request.POST, instance=comment)

        if form.is_valid():
            # printing the comment fields
            print ("comment: " + form.cleaned_data['commentContent'])
            # saving form data to our model
            comment = form.save(commit=False)
                # specifying the post that comment belongs to
            comment.post = post
            form.save()

    # navigating to detail page
    return redirect('blog:postDetail', post_id = post.pk)

def deleteComment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk = post_id)
    Comment.objects.filter(pk = comment_id).delete()
    return redirect('blog:postDetail', post_id = post.pk)
