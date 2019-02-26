from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.http import HttpResponse
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def postList(request):
    post_list = Post.objects.filter(publishedDate__lte = timezone.now()).order_by('-publishedDate')
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)
