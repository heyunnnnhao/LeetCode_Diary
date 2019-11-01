# my solution
def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()  # learned .sort() method
    return sum(nums[0::2])  # [start:finish:skip] same for list, string
    # it is faster with that 0. not a clue


# Runtime: 324 ms, faster than 91.36%
# Memory Usage: 16.4 MB, less than 6.06%

# solution 1
def arrayPairSum(self, A):
    return sum(sorted(A)[::2])
    # simpler than mine, learned that nums.sort() == sorted(nums)

# Runtime: 340 ms, faster than 47.09%
# Memory Usage: 16.3 MB, less than 6.06%

