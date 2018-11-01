from django import forms
from django.forms import widgets as wid

class UserForm(forms.Form):
    username_attr = {
        'id':'inputUsername',
        'class':'form-control',
        'placeholder':'请输入用户名/电子邮箱',
        'required':'',
        'autofocus':''
    }
    password_attr = {
        'id':'inputPassword',
        'class':'form-control',
        'placeholder':'请输入密码',
        'required':''
    }
    username = forms.CharField(label='Username',max_length=128,widget=forms.TextInput(attrs=username_attr))
    password = forms.CharField(label='Password',max_length=256,widget=forms.PasswordInput(attrs=password_attr))
