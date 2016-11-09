from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import json,datetime
from app import utils,models

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
            #更新在线状态
            user.userprofile.online = True
            user.userprofile.save()
            return HttpResponseRedirect('/chat/')
        else:
            login_err = 'Wrong username or password'
            return render(request, 'login.html',{'login_err':login_err})
    return render(request,'login.html')

def acc_logout(request):
    #更新在线状态
    request.user.userprofile.online = False
    request.user.userprofile.save()
    #登出
    logout(request)
    return HttpResponseRedirect('/')

global_msg_dic = {}

def dashboard(request):

    return render(request,'webqq/dashboard.html')

def send_msg(request):
    print(request.POST)
    data = json.loads(request.POST.get('data'))
    to_id = str(data.get('to_id'))
    user_obj = models.UserProfile.objects.get(id=to_id)
    contact_type = data.get('contact_type')
    data['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if contact_type == 'single':
        if to_id not in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat(request)#执行queue的初始化
        global_msg_dic[to_id].msg_queue.put(data)#把加上事件戳的消息对象放到队列
        print('\033[31;1mPush msg [%s] into user [%s] queue\033[0m' % (data['msg'],user_obj.name))
    elif contact_type == 'group':
        group_obj = models.QqGroup.objects.get(id=to_id)
        for member in group_obj.members.select_related():
            if member.id != request.user.userprofile.id:
                if str(member.id) not in global_msg_dic:
                    global_msg_dic[str(member.id)] = utils.Chat(request)
                global_msg_dic[str(member.id)].msg_queue.put(data)
                print('****global_msg_dic:',global_msg_dic)
                print('\033[31;1mPush msg [%s] into user [%s] queue\033[0m' % (data['msg'], member.name))
    elif contact_type == 'friend_request':
        if to_id not in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat(request)#执行queue的初始化
        global_msg_dic[to_id].msg_queue.put(data)#把加上事件戳的消息对象放到队列
        print('\033[31;1mPush friend request into user [%s] queue\033[0m' % (user_obj.name))
    elif contact_type == 'friend_accept':
        friend_obj = models.UserProfile.objects.get(id=request.user.userprofile.id);
        if friend_obj not in user_obj.friends.select_related():
            user_obj.friends.add(friend_obj)
            user_obj.save()
            print('\033[31;1mAdd friend [%s] to user [%s] \033[0m' % (friend_obj.name,user_obj.name))
        if to_id not in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat(request)#执行queue的初始化
        global_msg_dic[to_id].msg_queue.put(data)#把加上事件戳的消息对象放到队列
        print('\033[31;1mPush friend accept into user [%s] queue\033[0m' % (user_obj.name))

    return HttpResponse('ok')

def get_msg(request):
    uid = request.GET.get('uid')
    if uid:
        res = []
        if uid not in global_msg_dic:
            global_msg_dic[uid] = utils.Chat(request)
        res = global_msg_dic[uid].get_msg()
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps('uid not provided!'))