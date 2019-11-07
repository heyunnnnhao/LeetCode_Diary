# soution 1
def fib(N):
    if N <= 1:
        return N
    return fib(N - 1) + fib(N - 2)
    # nothing to say really, I blame the leetcode compiler for not compiling


# Runtime: 904 ms, faster than 25.93%
# Memory Usage: 12.8 MB, less than 100.00%

# solution 2
def fib(self, N: int) -> int:
    a, b = 0, 1
    for i in range(N):
        a, b = b, a + b
    return a
    # far better one.


# Runtime: 28 ms
# Memory Usage: 12.8 MB

