from itertools import accumulate


class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        """ """

        # breakpoint if arr[i] and arr[i-1] have different parity
        breakpoints = [0] + [0x01 & ~(nums[i] ^ nums[i + 1]) for i in range(len(nums) - 1)]

        # group by accumulating the breakpoints
        groups = list(accumulate(breakpoints))

        # if i and j are in the same group, True
        res = [groups[i] == groups[j] for i, j in queries]
        return res
