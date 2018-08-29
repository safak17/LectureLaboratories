from Queue import *         # We get all functions of Queue Class

# Created firstQueue
firstQueue = Queue()
firstQueue.enqueue(0)
firstQueue.enqueue(1)
print("firstQueue's Items")
firstQueue.printItems()
firstQueue.enqueue()
print("firstQueue's Items after popping")           # First In First Out
firstQueue.printItems()


# Created secondStack
secondQueue = Queue()
secondQueue.enqueue(0)
secondQueue.enqueue(1)
print("\nsecondQueue's Items")
secondQueue.printItems()


# Shallow copy (thirdStack is the shallow copy of firstStack.)
# Any change in thirdStack will affect the firstStack, and vise versa.
thirdQueue = firstQueue
print("\nthirdQueue's Items")
thirdQueue.printItems()
thirdQueue.enqueue(5)
print("\nthirdQueue's Items after pushing '5'")
thirdQueue.printItems()

print("\nBe aware that we pushed '5' to the thirdStack! But firstStack also has '5'.")
print("thirdQueue's Items")
thirdQueue.printItems()
print("firstQueue's Items")
firstQueue.printItems()
print("Because, thirdQueue is created from firstQueue, shallow copied!")
print("Any changes in thirdQueue will affect firstQueue, and vise versa.\n")


# Comparing Stacks
print("firstQueue == secondQueue ?  :   ", firstQueue.compare(secondQueue))
print("firstQueue == thirdQueue  ?  :   ", firstQueue.compare(thirdQueue))


# Reverse function doesn't return anything, just reverse the items of the Stack.
print("thirdQueue's Items before reversing")
thirdQueue.printItems()
thirdQueue.reverse()
print("thirdQueue's Items after reversing")
thirdQueue.printItems()

# getNewReversedStack returns a new stack with copied items of the base Stack.
fourthStack = thirdQueue.getNewReversedQueue()
print("\nfourthQueue's Items")
fourthStack.printItems()