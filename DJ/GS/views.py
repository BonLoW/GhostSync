from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserLoginForm
from .forms import ChatForm
from .forms import JoinNewGroupForm
from .models import User
from .models import Group
from .models import Message
from django.contrib.auth.decorators import login_required

# Create your views here.
def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username, password=password).exists():
                user = User.objects.get(username=username, password=password)
                return HttpResponseRedirect(reverse('home', args=(user.id,)))
            else:
                return HttpResponse("用户名或密码错误")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {'form': form})

@login_required
def Home(requset,user_id):
    if requset.method=="POST":
        form = JoinNewGroupForm(requset.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            if Group.objects.filter(name=group_name).exists():
                group = Group.objects.get(name=group_name)
                group.members.add(User.objects.get(id=user_id))
                group.save()
                return HttpResponseRedirect(reverse('home', args=(user_id,)))
            else:
                return HttpResponse("群名不存在")
    else:
        form = JoinNewGroupForm()
    user = User.objects.get(id=user_id)
    groups =Group.objects.filter(members=user)
    return render(requset, "home.html", {'username': user.username, 'groups': groups})

def Index(requset):
    return render(requset, "index.html")
