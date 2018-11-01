from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
# Create your views here.
def index(request):
    #登录了返回用户
    if request.session.get('is_login',None):
        username = request.session['user_name']
        return render(request,'myblog/index.html',{'username':username})
    return render(request,'myblog/index.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码错误'
            except:
                message = '用户不存在'
        return render(request,'myblog/login.html',{'login_form':login_form,'message':message})
    #get请求
    else:
        login_form = UserForm()
        return render(request,'myblog/login.html',{'login_form':login_form})

def register(request):
    pass
    return render(request,'myblog/register.html')

def logout(request):
    #未登录
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')