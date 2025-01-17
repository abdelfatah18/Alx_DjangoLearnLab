# blog/forms.py
from django import forms
from .models import Post
from taggit.forms import TagField, TagWidget  # Import TagField and TagWidget
from django.forms import widgets  # Import widgets

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget())  # Using TagWidget for tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
