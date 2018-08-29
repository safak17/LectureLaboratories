from Stack import *

# Palindrome is something that is equal to the reverse of it.
# As an example,    "madam" is a palindrome word, because the reverse of "madam" is also "madam".
# But,              "madame" is not a palindrome word, because the reverse of "madame" is "emadam".

stack = Stack()

userInput = input("Please, enter a word. I am going to check that if it is palindrome or not?")

for i in userInput:         # We pushed all items of userInput to the Stack. 'm', 'a', 'd', 'a', 'm'
    stack.push(i)

stack.printItems()

reversedStack = stack.getNewReversedStack()

if stack.compare(reversedStack):
    print("%s is palindrome!" % userInput)
else:
    print("%s is NOT palindrome!" % userInput)