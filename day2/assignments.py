from collections import deque
from ctypes import sizeof
from re import L
total = int(input("Enter the stack size :"))
stack = deque()
# Here we have added the the values into stack
for i in range(total):
    val = input()
    stack.append(val)
print(stack)

# deleting the element on top of stack


def topelement(stack):
    return stack.pop()


print(f"Deleted the top most value of stack is {topelement(stack)}")

# printing the max element


def getMax(stack):
    maxval = 0
    for i in range(len(stack)):
        popped = int(stack.pop())
        if maxval < popped:
            maxval = popped
    return maxval


print(f"The maximum value of stack is {getMax(stack)}")
