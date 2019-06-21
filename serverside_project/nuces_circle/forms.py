from django import forms

from .models import Post

class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body'
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(Post_form, self).save(**kwargs)
        instance.postedBy = user
        instance.save()
        return instance


