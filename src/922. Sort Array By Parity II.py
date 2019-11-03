# my solution
def sortArrayByParityII(self, A):
    out = [None] * len(A)  # create a list length is input
    list1, list2 = [], []  # create 2 list one for even and one for odd
    for i in range(len(A)):  # this loop fill the even and odd list
        if A[i] % 2 == 0:
            list1.append(A[i])
        else:
            list2.append(A[i])
    out[::2] = list1  # cross join two lists, list1 is even so it goes first
    out[1::2] = list2
    return out
    # not a good solution


# Runtime: 252 ms, faster than 58.46%
# Memory Usage: 16.2 MB, less than 8.70%

# solution 1
def sortArrayByParityII(self, A):
    even, odd = (a for a in A if not a % 2), (a for a in A if a % 2)
    return [y for x in zip(even, odd) for y in x]
    # same approach as mine, just more compact, slightly harder to understand


# solution 2
def sortArrayByParityII(self, A):
    my_odd = []
    my_even = []
    for a in A:
        if a & 1:  # AND statement, comparing if a ends with 1 in binary.
            my_odd.append(a)
        else:
            my_even.append(a)

    for i in range(0, len(A) // 2):
        A[i * 2] = my_even[i]
        A[i * 2 + 1] = my_odd[i]

    return A


# solution 3
def sortArrayByParityII(self, a):  # 2 pointer method, very brilliant
    i = 0  # pointer for even misplaced
    j = 1  # pointer for odd misplaced
    sz = len(a)

    # invariant: for every misplaced odd there is misplaced even
    # since there is just enough space for odds and evens

    while i < sz and j < sz:
        if (
            a[i] % 2 == 0
        ):  # if the first is even, move the pointer and check the third. if not, pointer stays
            i += 2
        elif (
            a[j] % 2 == 1
        ):  # if the second is odd, move the pointer and check the forth. if not, pointer stays
            j += 2
        else:
            # a[i] % 2 == 1 AND a[j] % 2 == 0
            # a pair of misplaced found, i and j are their respective pointer since they dont't move if misplaced found
            a[i], a[j] = a[j], a[i]  # swap
            i += 2  # move pointer
            j += 2

    return a


# not fast nor efficient, but brilliant algorithm

