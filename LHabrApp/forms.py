from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Post
        # fields = ['title', 'text']
        fields = '__all__'
        #options
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }