from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'postContent',)

        widgets = {
            'title': forms.TextInput(),
            'category': forms.TextInput(),
            'postContent': forms.Textarea(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commentContent',)

        widgets = {
            'commentContent': forms.Textarea(),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
