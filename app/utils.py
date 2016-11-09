import queue
from app import models

class Chat(object):
    def __init__(self,request):
        self.msg_queue = queue.Queue()
        self.request = request

    def get_msg(self):
        data = {
            'msg_list':self.get_dialog_msg(),
            'contact_dic':self.get_contact_dic(),
            'friend_request':self.get_friend_request(),
            'group_request':self.get_group_request(),
        }
        return data

    #获取在线好友,和所属群，用于更新好友状态和所属群列表
    def get_contact_dic(self):
        user_obj = models.UserProfile.objects.get(id=self.request.user.userprofile.id)
        friend_dic = user_obj.friends.select_related().filter(online=True).values('id','name','online')
        group_dic = user_obj.group_members.select_related().values('id','name')
        contact_dic = {
            'friends':list(friend_dic),
            'groups':list(group_dic)
        }
        return contact_dic

    #获取加好友请求
    def get_friend_request(self):
        pass
    #获取加群请求
    def get_group_request(self):
        pass

    def get_dialog_msg(self):
        new_msgs = []
        if self.msg_queue.qsize() > 0:#多条消息一次性返回
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get())
        else:#队列中无消息就阻塞60秒
            try:
                print('------- no new message, going to wait 60 seconds ------')
                new_msgs.append(self.msg_queue.get(timeout=60))
            except queue.Empty:
                print('\033[31;1mTimeout, no message for user [%s]\033[0m' % self.request.user.userprofile.name)
        print('\033[33;1mFound [%s] new messages for user [%s]\033[0m' % (len(new_msgs),self.request.user.userprofile.name))
        return new_msgs
