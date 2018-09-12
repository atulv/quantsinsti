from threading import Thread
import time
from decimal import Decimal
import requests, json

class Strategy(Thread):
    def __init__(self, queue, batch_size):
        Thread.__init__(self)
        self.queue = queue
        self.batch_size = batch_size

    def run(self):
        batch = self.queue.get(self.batch_size)
        if not batch:
            # no data available
            return
        try:
            avg = sum(batch)/len(batch)
        except ZeroDivisionError:
            pass
        else:
            try:
                r = requests.post('http://127.0.0.1:27015', data={'price': avg})
                if r.status_code == 200:
                    r = r.content
                    req_id = json.loads(r.replace("'",'"'))['id']

                    time.sleep(3)
                    r = requests.get('http://127.0.0.1:27015/?id=%s'%req_id)
                    if r.status_code == 200:
                        r = r.content
                        resp = json.loads(r.replace("'",'"'))['sold']
                    
                    if resp:
                        print avg*Decimal(1.1)
                    else:
                        print avg*Decimal(.9)
            except Exception, e:
                pass
