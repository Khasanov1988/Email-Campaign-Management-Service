from django import forms
from blog.models import *
from distribution.forms import StyleFormMixin


class PostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('is_published', 'views_count', 'made_date', 'slug',)


class PostUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('views_count', 'made_date', 'slug',)
