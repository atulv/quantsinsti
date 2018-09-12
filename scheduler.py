import data_manager
import queue
import strategy
import time

class Scheduler(object):
    def __init__(self, csv_path, batch_size):
        self.data_manager = data_manager.DataManager(csv_path, batch_size)
        self.queue = queue.Queue(self.data_manager)
        self.batch_size = batch_size

    def start(self):
        while True:
            task = strategy.Strategy(self.queue, self.batch_size)
            task.start()
            time.sleep(5)

sc = Scheduler('/Users/atulverma/Downloads/quantsinsti/data.csv', 5)
sc.start()
