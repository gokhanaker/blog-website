from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect, redirect
from django.http import HttpResponse
from blog.models import Post, Comment
from . import forms
from blog.forms import PostForm, CommentForm, UserForm
from django.utils import timezone
from django.contrib.auth import authenticate
# I used aliases here because I also have functions as login and logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def signup(request):
    registered = False
    user_form = UserForm()
    return render(request,'registration/signup.html',{'user_form':user_form, 'registered':registered})

def validateSignup(request):
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # save user form to database
            user = user_form.save()

            # hash the password and save it
            user.set_password(user.password)
            user.save()

            # registration Successful!
            registered = True
            return HttpResponseRedirect('/')

        else:
            print(user_form.errors)
            return HttpResponseRedirect('/registration/signup.html')

def login(request):
    login = False
    user_form = UserForm()
    return render(request,'registration/login.html',{'user_form':user_form,'login':login})

def validateLogin(request):

    if request.method == 'POST':
        # getting the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # if we have a user
        if user:
            # checking it the account is active
            if user.is_active:
                # log the user in.
                auth_login(request,user)
                # navigate to homepage
                return HttpResponseRedirect('/')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'blog:login', {})

@login_required
def logout(request):
    # log out the user.
    auth_logout(request)
    # return to homepage.
    return HttpResponseRedirect('/')


def postList(request):
    # getting all the blog posts and sorting them according to their created time
    post_list = Post.objects.filter(postCreatedDate__lte = timezone.now()).order_by('-postCreatedDate')
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)


def postDetail(request, post_id):
    # retrieving a post object from database using its primary key
    post = get_object_or_404(Post, pk = post_id)
    # sending that post object as a parameter to template
    return render (request, 'blog/post_detail.html', {'post': post})

@login_required
def newPost(request):
    # getting PostForm
    post_form = PostForm(request.POST)
    # sending post form as a parameter to template
    return render (request, 'blog/post_form.html', {'post_form': post_form})

# creates a blog post for drafts but not publish yet
@login_required
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

        else:
            print(form.errors)
            return HttpResponseRedirect('/blog/post_form.html')

@login_required
def editPost(request, post_id):
    # retrieving post object from database using its primary key
    post = get_object_or_404(Post, pk = post_id)

    currentUser = str(request.user)
    postAuthor = str(post.postAuthor)
    # print("current user is: " + currentUser)
    # print("author is: " + postAuthor)

    # if logged in user and post author are same user
    if postAuthor == currentUser:
        # sending post object to display its fields in the PostForm
        post_edit_form = PostForm(instance = post)
        return render(request, 'blog/post_edit.html', {'post_edit_form': post_edit_form})
    else:
        print("Someone tried to EDIT another user's post")
        return HttpResponse("You are NOT allowed to EDIT another user's post")


@login_required
def updatingEditedPost(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        # instance field is required to update the same post object NOT duplicate
        form = forms.PostForm(request.POST, instance=post)

        if form.is_valid():
            print ("title: " + form.cleaned_data['title'])
            print ("category: " + form.cleaned_data['category'])
            print ("content: " + form.cleaned_data['postContent'])
            # saving form data to our model
            form.save()
            # navigating to post detail page
            return redirect('blog:postDetail', post_id = post.pk)
        else:
            print(form.errors)
            return HttpResponseRedirect('/blog/post_edit.html')

@login_required
def deletePost(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    currentUser = str(request.user)
    postAuthor = str(post.postAuthor)

    # if logged in user and post author are same user
    if postAuthor == currentUser:
        # deleting a record from Post model
        Post.objects.filter(pk = post_id).delete()
        return redirect('/')
    else:
        print("Someone tried to DELETE another user's post")
        return HttpResponse("You are NOT allowed to DELETE another user's post")

@login_required
def likePost(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.postLikes += 1
    post.save()
    return redirect('blog:postDetail', post_id = post.pk)

@login_required
def addComment(request, post_id):
    comment_form = CommentForm(request.POST)
    return render (request, 'blog/comment_form.html', {'comment_form': comment_form})

@login_required
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

@login_required
def editComment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk = post_id)
    comment = get_object_or_404(Comment, pk = comment_id)

    currentUser = str(request.user)
    commentAuthor = str(comment.commentAuthor)

    # if logged in user and comment author are the same user
    if currentUser == commentAuthor:
        # sending comment object to display its fields in the comment form
        comment_edit_form = CommentForm(instance = comment)
        return render (request, 'blog/comment_edit.html', {'comment_edit_form': comment_edit_form})
    else:
        print("Someone tried to EDIT another user's comment")
        return HttpResponse("You are NOT allowed to EDIT another user's comment")


@login_required
def updateEditedComment(request, post_id, comment_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        comment = get_object_or_404(Comment, pk = comment_id)
        form = forms.CommentForm(request.POST, instance=comment)

        if form.is_valid():
            print ("comment: " + form.cleaned_data['commentContent'])
            comment = form.save(commit=False)
            # specifying the post that comment belongs to
            comment.post = post
            form.save()

    # navigating to detail page
    return redirect('blog:postDetail', post_id = post.pk)

@login_required
def deleteComment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk = post_id)
    comment = get_object_or_404(Comment, pk = comment_id)

    currentUser = str(request.user)
    commentAuthor = str(comment.commentAuthor)

    # if logged in user and comment author are the same user
    if currentUser == commentAuthor:
        # deleting comment object from comment model
        Comment.objects.filter(pk = comment_id).delete()
        return redirect('blog:postDetail', post_id = post.pk)
    else:
        print("Someone tried to DELETE another user's comment")
        return HttpResponse("You are NOT allowed to DELETE another user's comment")
