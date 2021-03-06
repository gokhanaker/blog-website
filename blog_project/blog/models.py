from django.db import models
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from django.utils import timezone
# importing User model for singup, login, logout
from django.contrib.auth.models import User

class Post(models.Model):
    # linking author with the current user
    postAuthor = CurrentUserField()
    title = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)
    postContent = models.TextField()
    postCreatedDate = models.DateTimeField(default = timezone.now)
    postLikes = models.IntegerField(default = 0)
    # upload to field is only for imageField and fileFields
    # user can choose to leave this field empty in that case, a default post image will be uploaded
    postImage = models.ImageField(upload_to="blog_post_images/", default="default.png", blank= True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    commentAuthor = CurrentUserField()
    commentContent = models.TextField()
    commentCreatedDate = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.commentContent
