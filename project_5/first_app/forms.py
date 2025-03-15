from django import forms
from django.core import validators
# widgets = field in html input
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name",required=True,
    help_text="Total length must be with 8 charecter",
    widget=forms.TextInput(attrs={'type':'name','placeholder':'Enter Your Full Name',
    'id':'name','class':'Class1 Class2'}))

    Text = forms.CharField(label="Description",required=True,help_text="Total length must be within 30 character",
    widget=forms.Textarea(attrs={'placeholder':'Text','id':'text-area','class':'text-area'}))
    
    file = forms.FileField(required=True)
    
    email = forms.EmailField(label="User Email",required=True,)
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    
    age = forms.CharField(label="Age",required=True,widget=forms.NumberInput)
    
    birthday = forms.CharField(label="Birthday",required=True,widget=forms.DateInput(attrs={'type':'date'}))
    
    appoinment = forms.CharField(required=True,widget=forms.DateInput(attrs={'type':'datetime-local'}))
    
    check = forms.BooleanField(required=True)
    
    CHOICES = [('S','Simple'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,required=True,widget=forms.RadioSelect)
    
    MEAL = [('P','Pizza'),('K','Kachi'),('B','Burger')]
    food = forms.MultipleChoiceField(choices=MEAL,required=True,widget=forms.CheckboxSelectMultiple)


class studentForm(forms.Form):
    name = forms.CharField(label="Full Name",required=True,
    help_text="Total length must be with 8 charecter",
    widget=forms.TextInput(attrs={'type':'name','placeholder':'Enter Your Full Name',
    'id':'name','class':'Class1 Class2'}),validators=[validators.MinLengthValidator(7,
    message='Enter a name with at least 8 characters')])
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 7:
    #         raise forms.ValidationError("Enter a name with at least 8 characters")
    #     return valname

    email = forms.CharField(label="User Email",required=True,widget=forms.TextInput(attrs=
    {'type':'email','placeholder':'Enter your email'}),validators=[validators.EmailValidator
    (message='Enter a valid email')])
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data.get('name')
    #     valemail = self.cleaned_data.get('email')
    #     if len(valname) < 7:
    #         raise forms.ValidationError("Enter a name with at least 8 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    def check_text(value):
        if len(value) < 10:
            raise forms.ValidationError("You must be include upto 10 character of message`")

    text = forms.CharField(widget=forms.TextInput,validators=[check_text])
    age = forms.IntegerField(label='Age',required=True,widget=forms.NumberInput,validators=[
    validators.MaxValueValidator(30,message="your maximum number 30"),
    validators.MinValueValidator(18,message='Your minimum value 18')])

    birthday = forms.CharField(label="Birthday",required=True,widget=forms.DateInput(attrs={'type':'date'}))
    
    CHOICES = [('Male','Male'),('Female','Female')]
    size = forms.ChoiceField(choices=CHOICES,required=True,widget=forms.RadioSelect)
    file = forms.FileField(validators=[validators.FileExtensionValidator
    (allowed_extensions=['pdf','png'],message='You must be send .pdf')],required=False)
    check = forms.BooleanField(required=True)

class passwordform(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        val_pass = self.cleaned_data.get('password')
        val_conpass = self.cleaned_data.get('confirm_password')
        val_name = self.cleaned_data.get('name')
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 8:
            raise forms.ValidationError("You must be include 8 character")
        # return cleaned_data