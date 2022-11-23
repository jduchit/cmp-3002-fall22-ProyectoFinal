import ctypes

class Queue(object):
    def __init__(self, n):

        self.l = 0
        self.n = n
        self.queue = self._create_queue(self.n)    
    
    def _create_queue(self, n):

        return (n * ctypes.py_object)()
    
    def enqueue(self, item):

        if self.l == self.n:
            raise ValueError("no more capacity")
        self.queue[self.l] = item
        self.l += 1
        
    def dequeue(self):

        c = self.queue[0]
        for i in range(1,self.l):
            self.queue[i-1] = self.queue[i]
        self.queue[self.l - 1] = ctypes.py_object
        self.l -= 1
        return c
    
    def first(self):

        return self.queue[0]
    
    def full(self):

        if self.l == self.n:
            return True
        return False

    def empty(self):

        if self.l == 0:
            return True
        return False
  
    def size(self):

        return self.l