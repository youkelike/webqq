import queue

class Chat(object):
    def __init__(self):
        self.msg_queue = queue.Queue()

    def get_msg(self):
        new_msgs = []
        if self.msg_queue.qsize() > 0:#多条消息一次性返回
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get())

        return new_msgs