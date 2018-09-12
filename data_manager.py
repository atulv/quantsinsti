from collections import deque
from decimal import Decimal
import time

class DataManager(object):
    def __init__(self, filename, batch_size):
        self.source = open(filename)
        self.batch_size = batch_size
        self.buffer = deque([], 5*batch_size)
        self.unused = 0
        
    def get_next_batch(self):
        if self.unused:
            _list = []
            _count = self.batch_size
            while _count:
                try:
                    _list.append(self.buffer.popleft())
                    _count -= 1
                    self.unused -= 1
                except:
                    break
            return _list
        else:
            _count = 5*self.batch_size
            while _count:
                try:
                    self.buffer.append(Decimal(self.source.next().split(',')[1].split()[0]))
                    _count -= 1
                    self.unused += 1
                except: 
                    # EOF
                    break

            if self.unused:
                return self.get_next_batch()
            else:
                return []
