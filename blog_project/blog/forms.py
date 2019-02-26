from django import forms
from .models import Post, Comment

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
