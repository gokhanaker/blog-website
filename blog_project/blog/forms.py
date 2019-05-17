from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'postContent', 'postImage')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            # self.helper.form_show_errors = False 


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commentContent',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
