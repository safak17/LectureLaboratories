from copy import deepcopy

class Stack:
    """A basic Stack implementation using lists"""          # docstring
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()     # If no index is specified, a.pop() removes and returns the last item in the list.

    def getTopItem(self):
        return self.items[-1]       # Returns the item which is at the top of the Stack.

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def compare(self, otherStack):
        return self.items == otherStack.items

    def reverse(self):
        self.items.reverse()

    def getNewReversedStack(self):
        temp = deepcopy(self)
        temp.reverse()
        return temp

    def printItems(self):
        print(self.items)
