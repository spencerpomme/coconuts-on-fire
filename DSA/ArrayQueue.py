# python implemented queue ADT
# A new exception class defined for handling empty errors

class Empty(Exception):
    '''
    Error attempting to access an element from an empty container.
    '''
    pass

class ArrayQueue:
    '''FIFO queue implementation using a python list as underlying storage.'''
    DEFAULT_CAPACITY = 10                                   # moderate capacity for all
                                                            # new queues
    def __init__(self):
        '''Create an empty queue.'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        '''Return the number of elements in the queue.'''
        return self._size

    def is_empty(self):
        '''Return True if the queue is empty.'''
        return self._size == 0

    def first(self):
        '''Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.'''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''Remove and return the first element of the queue(i.e.,FIFO).
    Raise Empty exception if the queue is empty.'''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)   # i.e.,DEFAULT_CAPACITY
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)                # shrink list by 1/2 after
        return answer                                       # dequeue if shorter than 1/4
                                                            
    def enqueue(self, e):
        '''Add an element to the back of queue.'''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))               # double the array size
        avail = (self._front +self._size) % len(self._data)
                                                            # self._size is current element
                                                            # number (before enqueue)
        self._data[avail] = e
        self._size += 1                                     # new size after enqueue

    def _resize(self, cap):
        '''Resize to a new list of capacity >= len(self)'''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):                         # self._size here is old size
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0                                     # self._front realigned
        
        

    
    
