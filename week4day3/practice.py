# binary search tree
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        # if the value is already present then return
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = BST(data)

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()

        return elements


def builttree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root


ele = [20, 8, 7, 21, 9, 7, 22, 40]
tree = builttree(ele)
print(tree.inorder())
