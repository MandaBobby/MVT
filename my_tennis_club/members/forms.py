from django import forms
from .models import Contact,Registration

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'address']

class ValueForm(forms.Form):
    input_value = forms.IntegerField(label='Enter a value', min_value=0)



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = ['firstname','lastname','email','password','confirm_password']
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)


from django import forms
from .models import Product

class RegistrationForm(forms.Form):
    firstname = forms.CharField(max_length=30, label='First Name')
    lastname = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    role= forms.ChoiceField(choices=[("admin","ADMIN"),("user","USER")])

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    role= forms.ChoiceField(choices=[("admin","ADMIN"),("user","USER")])

class ProductForm(forms.ModelForm):
 class Meta:  
    model = Product
    fields = ['name', 'quality','quantity']

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']  
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'enter smthg bhayya!'})
}


from django import forms
from .models import ProductRegistration

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('user', 'User')])

    class Meta:
        model = ProductRegistration
        fields = ['firstname', 'lastname', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('user', 'User')])
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quality','quantity']


from django import forms


class SuperuserCreationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    is_staff =True
    is_superuser= True

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    

from django import forms
from .models import RegistrationDatabase

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=123)
    email= forms.CharField(max_length=123)
    password = forms.CharField(max_length=123, widget=forms.PasswordInput)
    confirm_password =forms.CharField(max_length=128, widget=forms.PasswordInput)