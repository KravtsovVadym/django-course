from django import forms
from weblog.models import Post

# >---------------------------------------<
# (Post creation form) -------------------<
# >---------------------------------------<
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'article',
            'tags',
            'image'
        ]
        
    
    

