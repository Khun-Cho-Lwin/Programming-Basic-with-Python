from pyqueue import Queue
class PQueue:
    def __init__(self):
        self.items = {}
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self,item,priority = 0):
        if priority not in self.items:
            self.items[priority] = Queue()
            queue = self.items[priority]
            queue.enqueue(item)
    def dequeue(self):
        keys = list(self.items.keys())
        if len(keys) > 0:
            cursor = keys[-1]
            myqueue = self.items[cursor]
            val = myqueue.dequeue()
            if myqueue.size() == 0:
                del self.items[cursor]
                return val
                return ""
    def size(self):
        size = 0
        for key in self.items.keys():
            size = size + self.items[key].size()
            return size

from pqueue import PQueue
p = PQueue()
p.enqueue("HELLO",1)
p.enqueue("H",2)
p.enqueue("E",5)
p.enqueue("L",3)
p.enqueue("O",3)
p.enqueue("Sample",9)
# 7
print(p.size())
#Sample
print(p.dequeue())
#E
print(p.dequeue())
#4
print(p.size())
#L
print(p.dequeue())
#O
print(p.dequeue())
#H
print(p.dequeue())
#1
print(p.size())
