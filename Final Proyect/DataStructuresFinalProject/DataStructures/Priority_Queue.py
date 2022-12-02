import ctypes

class PriorityQueue(object):
    """
    Implementation of the queue data structure
    """

    def __init__(self, n):
        self.l = 0
        self.n = n
        self.queue = self._create_queue(self.n)        
    
    def _create_queue(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()
    
    def enqueue(self, item):
        """
        Add new item to the queue
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        
        self.queue[self.l] = item
        self.l += 1
        j = self.l - 2
        while (j >= 0) and (item[1] > self.queue[j][1]):
            self.queue[j+1] = self.queue[j]
            j -= 1
        self.queue[j+1] = item    
        
    def dequeue(self):
        """
        Remove item with lowest key
        """
        x = self.queue[self.l-1]
        self.l -= 1
        return x[0]