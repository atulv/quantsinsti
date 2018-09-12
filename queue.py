from collections import deque
import time

class Queue(object):
    def __init__(self, data_manager):
        self.queue = deque()
        self.data_manager = data_manager

    def get(self, cnt):
        ret = []
        while cnt:
            try:
                ret.append(self.queue.popleft())
                cnt -= 1
            except IndexError:
                self.queue.extend(self.data_manager.get_next_batch())
        return ret
        
