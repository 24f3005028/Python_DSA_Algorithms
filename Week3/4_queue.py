"""
Queue
    Implementing Queue class  -  FIFO (First In First Out)
        Data Memebers: queue[] List of integers
        Functions: constructor __init__(), isEmpty(), enQueue(), deQueue() and __str__()
"""

class Queue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return self.queue == []
    def enQueue(self, v):
        return self.queue.append(v)
    def deQueue(self):
        v=None
        if not self.isEmpty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    def __str__(self):
        return str(self.queue)
    

q = Queue()
q.enQueue(2)
q.enQueue(4)
q.enQueue(1)
q.enQueue(7)
q.enQueue(5)
print(q)
print(q.deQueue())