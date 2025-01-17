from django import forms
from .models import Comment
from .models import Post, Tag
from taggit.forms import TagField  # If using django-taggit


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'rows': 4, 'placeholder': 'Write your comment here...'})



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content cannot be empty.")
        if len(content) < 10:
            raise forms.ValidationError("Comment must be at least 10 characters long.")
        return content



class PostForm(forms.ModelForm):
    tags = TagField()  # Allows adding tags using django-taggit

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
