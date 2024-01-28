from django import forms
from .models import User
from .models import Group
from .models import Message

class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30)
    password = forms.CharField(label='密码', max_length=30, widget=forms.PasswordInput)

class ChatForm(forms.Form):
    message = forms.CharField(label='消息', max_length=1000, widget=forms.Textarea)

class JoinNewGroupForm(forms.Form):
    group_name = forms.CharField(label='群名', max_length=30)