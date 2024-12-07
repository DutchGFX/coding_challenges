import math


def isPossible(nums: list[int], maxOps: int, maxSize: int):
    """
    Determines if it is possible to achieve a max bag size of `maxSize`
    in `maxOperations`

    We do so by splitting the largest intervals until we hit maxOps or
    the desired maximum size

    Parameters
    ----------
    nums : list[int]
        balls in each bag, sorted in descending order
    maxOps : int
        maximum times we can split a bag
    maxSize : int
        desired maximum size

    Returns
    -------
    b : bool
        True if we can achieve the desired bag size in the max number
        of operations
    """
    n = 0  # number of operations we've performed
    for val in nums:  # for every value
        if val <= maxSize:  # if we don't need to split
            return True

        # increment the count
        n += math.ceil(val / maxSize) - 1

        # if the count is too large, return False
        if n > maxOps:
            return False
    return True


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        """
        Computes the minimum possible largest bag size

        Notes
        -----
        We use a binary search to find the first (smallest) bag size.
        We know that 0 is impossible, so that's too small, and we know
        that `max(nums)` is at least big enough, since we already
        satisfy that without conducting any operations. We initialize
        our binary search with those values.

        Parameters
        ----------
        nums : list[int]
            balls in each bag, sorted in descending order
        maxOps : int
            maximum times we can split a bag

        Returns
        -------
        m : int
            minimum maximum bag size
        """
        # sort in desce
        nums.sort(reverse=True)

        # binary search
        left = 0  # initial point to the left
        right = nums[0]  # since we sorted in descending order
        while left < right - 1:
            mid = (left + right) // 2  # compute midpoint
            midFunc = isPossible(nums, maxOperations, mid)
            left = left if midFunc else mid
            right = mid if midFunc else right
        return right
