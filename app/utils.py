import queue

class Chat(object):
    def __init__(self):
        self.msg_queue = queue.Queue()

    def get_msg(self,request):
        new_msgs = []
        if self.msg_queue.qsize() > 0:#多条消息一次性返回
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get())
        else:#队列中无消息就阻塞60秒
            try:
                print('------- no new message, going to wait 60 seconds ------')
                new_msgs.append(self.msg_queue.get(timeout=60))
            except queue.Empty:
                print('\033[31;1mTimeout, no message for user [%s]\033[0m' % request.user.userprofile.name)
        print('\033[33;1mFound [%s] new messages for user [%s]\033[0m' % (len(new_msgs),request.user.userprofile.name))
        return new_msgs