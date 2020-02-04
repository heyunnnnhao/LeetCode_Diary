# solution 1
def hammingDistance(self, x, y):
    return bin(x ^ y).count("1")
    """
    ^ is a Bitwise operator, means Bitwise XOR gate. 
    bin() returns the binary string equivalent to the given integer.
    .count() returns count of how many times a given object occurs in list or string.
    """


# Runtime: 40 ms, faster than 37.84%
# Memory Usage: 13.8 MB, less than 8.70%

# solution 2
def hammingDistance(self, x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    for _ in range(32):
        count += xor & 1
        xor = xor >> 1
    return count


# https://www.tutorialgateway.org/python-bitwise-operators/ more on bitwise operator
# Runtime: 52 ms
# Memory Usage: 13.8 MB

# solution 3
def hammingDistance(self, x: int, y: int) -> int:
    return sum(((x ^ y) >> n) & 1 != 0 for n in range(32))
    # same as solution 1, counting how many 1 in a final joined binary number


# Runtime: 40 ms
# Memory Usage: 13.8 MB
# meaningess comment here

