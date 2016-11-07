from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        #验证动作
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            #登录动作
            login(request,user)
            return HttpResponseRedirect('/chat/')
        else:
            login_err = 'Wrong username or password'
            return render(request, 'login.html',{'login_err':login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):

    return render(request,'webqq/dashboard.html')