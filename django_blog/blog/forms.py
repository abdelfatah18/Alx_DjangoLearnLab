from django import forms
from taggit.forms import TagWidget
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'body']  # adjust field names to your model
        # Example of adding widgets or validation rules:
        widgets = {
            'author_name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_body(self):
        body = self.cleaned_data.get('body', '')
        if len(body.strip()) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return body
