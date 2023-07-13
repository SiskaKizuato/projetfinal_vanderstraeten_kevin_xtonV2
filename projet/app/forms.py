from django import forms
from .models import Profile, Article, Category, ContactInfo

class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['location', 'phone', 'email', 'fax']
        
