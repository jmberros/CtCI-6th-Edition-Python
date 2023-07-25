class NoSuchElementException(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        t = QueueNode(item)
        
        if self.last is None:
            self.last.next = t
        
        self.last = t

        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.is_empty():
            raise NoSuchElementException

        data = self.first.data
        self.first = self.first.next
        if self.is_empty():
            self.last = None

        return data

    def peek(self):
        if self.is_empty():
            raise NoSuchElementException

        return self.first.data

    def is_empty(self):
        return self.first is None
