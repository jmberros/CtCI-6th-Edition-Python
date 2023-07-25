class EmptyStackException(Exception):
    pass


class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

### Second definition ###

class Stack:
    def __init__(self):
        self.top = None

    def __repr__(self):
        values = []
        node = self.top
        while node:
            values.append(str(node.value))
            node = node.next
        return f"{self.__class__.__name__}(" + ".".join(reversed(values)) + ")"

    def push(self, value):
        node = StackNode(value=value)
        node.next = self.top
        self.top = node

    def pop(self):
        self.raise_if_empty()
        item = self.top
        self.top = item.next
        return item.value

    def peek(self):
        self.raise_if_empty()
        return self.top.value

    def raise_if_empty(self):
        if self.is_empty():
            raise EmptyStackException

    def is_empty(self):
        return self.top is None

### First definition ###

# class Stack:
#     def __init__(self):
#         self.top = None

#     def __repr__(self):
#         values = ""
#         item = self.top
#         while item:
#             values += f"{item.data}/"
#             item = item.next
#         return f"{self.__class__.__name__}({values})"

#     def pop(self):
#         if self.top is None:
#             raise EmptyStackException

#         item = self.top
#         self.top = self.top.next
#         return item

#     def push(self, item):
#         t = StackNode(item)
#         t.next = self.top
#         self.top = t

#     def peek(self):
#         if self.top is None: 
#             raise EmptyStackException

#         return self.top.data

#     def is_empty(self):
#         return self.top is None
