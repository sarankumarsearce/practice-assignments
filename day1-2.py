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
                print(temp.data)
                temp = temp.next


P = int(input("Tell the number of nodes :"))
print("Type the values of each node")
data = [input() for i in range(P)]

SL = Singlelinkedlist()
print("The values of linked list are: ")
for i in range(0, P-1):
    n = Node(data[i])
    SL.head = n
    n1 = Node(data[i+1])
    n.next = n1
    SL.display()
