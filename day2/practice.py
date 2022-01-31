class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singlelist:
    def __init__(self):
        self.head = None

    def begin(self, data):
        nb = Node(data)
        self.head = nb
        nb.next = n

    def last(self, data):
        ln = Node(data)
        n2.next = ln
        ln.next = None

    def middle(self, pos, data):
        mn = Node(data)
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        mn.next = temp.next
        temp.next = mn

    def display(self):
        if self.head is None:
            print("Empty list")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


sl = singlelist()
n = Node(100)
sl.head = n
n1 = Node(200)
n.next = n1
n2 = Node(300)
n1.next = n2
sl.begin(76)
sl.last(23)
sl.middle(4, 96)
sl.display()
