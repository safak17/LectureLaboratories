from copy import deepcopy

class Queue:
    """A basic Stack implementation using lists"""          # docstring
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)    # If no index is specified, a.pop() removes and returns the last item in the list.

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def compare(self, otherStack):
        return self.items == otherStack.items

    def reverse(self):
        self.items.reverse()

    def getNewReversedQueue(self):
        temp = deepcopy(self)
        temp.reverse()
        return temp

    def printItems(self):
        print(self.items)