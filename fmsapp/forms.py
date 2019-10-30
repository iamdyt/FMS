from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . models import Dam, Staff, Department,Fish,TimeLine,Sales,Debtors
from django.contrib.auth import get_user_model


class LoginForm (AuthenticationForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))

    class Meta:
        model = get_user_model()
        fields = '__all__'
class RegisterForm (UserCreationForm):
    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'First Name '}))
    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Last Name '}))
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Username '}))
    password1 = forms.CharField(label='Password',max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Password '}))
    password2 = forms.CharField(label='Confirm Password',max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control p-4 mb-3', 'placeholder':'Confirm Password '}))

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','password1','password2','image']
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

class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Fish Name'}),
            'types':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Fish Type'}),
            'HarvestDate':forms.TextInput(attrs={'class':'form-control mb-3 ','placeholder':'Harvest Date'}),
            'total':forms.NumberInput(attrs={'class':'form-control mb-3','placeholder':'Total'}),
            'ímage':forms.FileInput(attrs={'class':'form-control mt-2'})
        }

class HarvestForm(forms.ModelForm):
    class Meta:
        model = TimeLine
        fields = '__all__'
        widgets = {
            'number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Fish Harvested'}),
            'dam':forms.TextInput(attrs={'class':'form-control','placeholder':'From which Dam'}),
            'others':forms.Textarea(attrs={'class':'form-control','placeholder':'Other Note here'})
        }

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields =['types','weight','quantity','amount','price']
        widgets = {
            'types':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g Tilapia'}),
            'amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price per one per weight','id':'amt'}),
            'weight':forms.NumberInput(attrs={'class':'form-control','placeholder':'Fish weight'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Fish','id':'qty'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid','id':'prc','readonly':'readonly'})

        }

class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'file_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Staff-file No'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Number of Fish'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Staffer Department' }),
            'amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Amount to be paid'}),
            'signature':forms.ClearableFileInput(attrs={'class':'form-control'})

        }
        