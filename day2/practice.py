# once again starting with singlylinked list
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link


class Single:
    def __init__(self):
        self.head = None

    def end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        temp = self.head
        while temp.link:
            temp = temp.link
            print(temp.data, "-->", end="")

        temp.link = Node(data, None)

    def insert(self, datalist):
        self.head = None
        for i in datalist:
            self.end(i)


sll = Single()
sll.insert([1, 2, 3, 4])


# sll.head = n
# n1 = Node(200)
# n.link = n1
# n2 = Node(300)
# n1.link = n2
