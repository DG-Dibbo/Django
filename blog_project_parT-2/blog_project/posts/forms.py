from django import forms
from .models import Post

class PageForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']
        
        # fields = ['name','bio','phone'] # sudu ay 3ta item dekhabe
        # exclude = ['bio'] # bio model bade bki sob dekhabe