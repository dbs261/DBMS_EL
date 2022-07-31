from django.forms import ModelForm, Textarea
from .models import Post

class PostForm(ModelForm):
    # resp = ""

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title','body']
        widgets = {'body':Textarea}