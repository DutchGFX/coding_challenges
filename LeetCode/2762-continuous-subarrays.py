from heapq import heapify, heappop, heappush


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        """
        TODO
        """
        # the heaps keep track of the starting indices
        cnt = 0
        start = 0  # starting index
        minheap, maxheap = [], []

        # for every index `j`, we find all sub-arrays ending at index `j`
        for end in range(len(nums)):
            # push to heaps
            heappush(minheap, (nums[end], end))
            heappush(maxheap, (-nums[end], end))

            # find the left-most index such that we are still within +-2
            while -maxheap[0][0] - minheap[0][0] > 2:
                # try to increase the left index
                start += 1
                while maxheap[0][1] < start:
                    heappop(maxheap)
                while minheap[0][1] < start:
                    heappop(minheap)

            # all subarrays from [start, end] are valid, including [start+1, end], etc
            cnt += end - start + 1
        return cnt
