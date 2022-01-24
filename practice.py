# from collections import deque
# a = [1, 2, 3]
# print(a)
# two dimensional array

# b = [[[1, 2], [8, 9]], [3, 4]]
# print(b[0][1][1])

# a.append(4)
# a.insert(1, 9)
# print(a)
# a.pop()
# print(a)

# Implementing stack using deque in python
# stack = deque()
# stack.append("first")
# stack.append("second")
# stack.append("third")
# print(stack)
# stack.pop()
# print(stack)

# Implementing queue using deque in python
# q = deque()
# q.appendleft(5)
# q.appendleft(6)
# q.appendleft(7)
# print(q)

# Singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singlelinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
                temp = temp.next


SL = Singlelinkedlist()
n = Node(100)
SL.head = n
n1 = Node(200)
n.next = n1
n2 = Node(300)
n1.next = n2
SL.display()
