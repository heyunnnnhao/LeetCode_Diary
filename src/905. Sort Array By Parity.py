# my solution, works but not good enough
def sortArrayByParity(A):
    even = []
    odd = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
    return even + odd


# Runtime: 92 ms, faster than 84.83%
# Memory Usage: 14.3 MB, less than 5.19%

# solution 1
def sortArrayByParity(self, A):
    return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
    # same as mine, just more compact and sophisticated, result worse than mine


# solution 2
def sortArrayByParity(self, A):
    i, j = 0, len(A) - 1  # start and end
    while i < j:
        if A[i] % 2 > A[j] % 2:  # compare start and end
            A[i], A[j] = A[j], A[i]  # if needed, swap

        if A[i] % 2 == 0:
            i += 1  # start plus one
        if A[j] % 2 == 1:
            j -= 1  # end minus one

    return A  # return swaped list


# Runtime: 88 ms, faster than 95.84%
# Memory Usage: 14.3 MB, less than 5.19%

