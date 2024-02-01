from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from .models import *
from .forms import *

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #实现登录功能
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                request.session['username'] = username
                login(request,user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse('用户名或密码错误')
        else:
            return HttpResponse('表单不合法')
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})


def Home(request):
    if 'username' in request.session:
        username = request.session['username']
        user = User.objects.get(username=username)
        groups = Group.objects.filter(members=user)
        return render(request,'home.html',{'groups':groups,'username':username})
    else:
        return HttpResponse('请先登录')