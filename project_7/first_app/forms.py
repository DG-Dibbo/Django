from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # fields = ['name','roll'] sudu name & roll dekhabe display te
        # exclude = ['father_name'] sudu father_name dekhabe nah baki sob kisu dekhabe
        fields = '__all__' #ata use korle sob kisu dekhabe ModelForm er
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student ID',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'roll': forms.NumberInput(attrs={'placeholder': 'Roll ID'}),
            'father_name': forms.TextInput(attrs={'placeholder': 'Enter Your Father Name'}),
            'address': forms.Textarea(attrs={'placeholder': 'Tell me your details', 'rows': 3}),
        }
        help_texts ={
            'name': 'Enter Your Full Name',
        }
        error_messages ={
            'name':{'required':'Enter Your Name'}
        }