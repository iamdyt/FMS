from django.contrib.auth.forms import AuthenticationForm
from django import forms
from . models import Dam, Staff, Department


class LoginForm (AuthenticationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'au-input au-input--full', 'placeholder':'Username '}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'au-input au-input--full', 'placeholder':'Password '}))

class DamForm (forms.ModelForm):

    class Meta:
        model = Dam
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dam Unique Name'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'no_fishes':forms.TextInput(attrs={'class':'form-control', 'placeholder':'No of Fishes in this Dam'}),
            'fish_categories':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Categories'}),
            'location':forms.Textarea(attrs={'class':'form-control text-justify', 'placeholder':'Dam Location','rows':2}),
            'about':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More Info','rows':2}),
        }

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = "__all__"
        widgets={
            
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'stipend':forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'state':forms.Select(attrs={'class':'form-control','placeholder':'Salary'}),
            'country':forms.TextInput(attrs={'class':'form-control','placeholder':'country'}),
            'department':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'work_description':forms.Textarea(attrs={'class':'form-control','placeholder':'Work Description','rows':2, 'cols':4}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Department Name'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'})
        }