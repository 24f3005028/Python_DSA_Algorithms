"""
BFS - Breadth First Search

Using Queue from Week 3
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
    

