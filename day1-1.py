# First question
Q = int(input("Enter the size of array : "))
P = [input() for i in range(Q)]
# Got the value of Q and elements of P using list comprehension


def reverseArray(P):
    return P[::-1]


# Calling the P-array and reverseArray function
print(P)
print(reverseArray(P))
