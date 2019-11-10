# solution 1
def buddyStrings(self, A, B):
    if len(A) != len(B):
        return False
    if A == B and len(set(A)) < len(A):  # don't understand that
        return True
    dif = [
        (a, b) for a, b in zip(A, B) if a != b
    ]  # create a tuple with all the difference pairs
    return (
        len(dif) == 2 and dif[0] == dif[1][::-1]
    )  # if the total pairs of different is 2 and they are reverse


# Runtime: 28 ms, faster than 99.43%
# Memory Usage: 12.8 MB, less than 100.00%

