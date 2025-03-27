from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['name','bio','phone'] # sudu ay 3ta item dekhabe
        # exclude = ['bio'] # bio model bade bki sob dekhabe