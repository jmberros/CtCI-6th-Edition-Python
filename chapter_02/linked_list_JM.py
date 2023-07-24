from typing import List


class LinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        # self.prev = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        else:
            return self.value == other.value


class LinkedList:
    def __init__(self, values: List[int] = None):
        self.head = None
        self.tail = None

        if values:
            for value in values:
                self.add(value)

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next

    def __len__(self):
        return sum(1 for node in self)
                
    def add(self, value: int):
        n = LinkedListNode(value)
        if self.head is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def delete(self, value: int):
        n = self.head

        if n is None:
            return

        if n.value == value:
            self.head = n.next  # Head shifts

        while n.next is not None:
            if n.next.value == value:
                n.next = n.next.next  # Skip a node
            n = n.next

    def __repr__(self):
        n = self.head
        values = []
        while n is not None:
            values.append(str(n))
            n = n.next
        return "LinkedList(" + "-".join(values) + ")"

    def __eq__(self, other):
        return str(self) == str(other)  # Hack