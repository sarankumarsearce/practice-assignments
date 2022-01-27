from tkinter.tix import MAX


class Hash:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def hash(self, key):
        h = 0
        for i in key:
            h = h+ord(i)
        return h % self.MAX

    def add(self, key, val):
        k = self.hash(key)
        self.arr[k] = val

    def get(self, key):
        ans = self.hash(key)
        return self.arr[ans]


h = Hash()
print(h.add('saran', 2))
print(h.add('dhoni', 89))
print(h.arr)
print(h.get('saran'))
