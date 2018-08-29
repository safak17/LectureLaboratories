from Stack import *         # We get all functions of Stack Class

# Created firstStack
firstStack = Stack()
firstStack.push(0)
firstStack.push(1)
print("firstStack's Items")
firstStack.printItems()
firstStack.pop()
print("firstStack's Items after popping")           # Last In First Out
firstStack.printItems()


# Created secondStack
secondStack = Stack()
secondStack.push(0)
secondStack.push(1)
print("\nsecondStack's Items")
secondStack.printItems()


# Shallow copy (thirdStack is the shallow copy of firstStack.)
# Any change in thirdStack will affect the firstStack, and vise versa.
thirdStack = firstStack
print("\nthirdStack's Items")
thirdStack.printItems()
thirdStack.push(5)
print("\nthirdStack's Items after pushing '5'")
thirdStack.printItems()

print("\nBe aware that we pushed '5' to the thirdStack! But firstStack also has '5'.")
print("thirdStack's Items")
thirdStack.printItems()
print("firstStack's Items")
firstStack.printItems()
print("Because, thirdStack is created from firstStack, shallow copied!")
print("Any changes in thirdStack will affect firstStack, and vise versa.\n")


# Comparing Stacks
print("firstStack == secondStack ?  :   ", firstStack.compare(secondStack))
print("firstStack == thirdStack  ?  :   ", firstStack.compare(thirdStack))


# Reverse function doesn't return anything, just reverse the items of the Stack.
print("thirdStack's Items before reversing")
thirdStack.printItems()
thirdStack.reverse()
print("thirdStack's Items after reversing")
thirdStack.printItems()

# getNewReversedStack returns a new stack with copied items of the base Stack.
fourthStack = thirdStack.getNewReversedStack()
print("\nfourthStack's Items")
fourthStack.printItems()