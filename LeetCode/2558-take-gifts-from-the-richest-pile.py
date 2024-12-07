import math
from heapq import heapify, heappop, heappush


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        Use a maxheap to keep track of the largest gift

        Parameters
        ----------
        gifts : list[int]
            gift pile sizes
        k : int
            number of seconds

        Returns
        -------
        cnt : int
            number of gifts remaining after `k` seconds
        """
        # convert into a maxheap by using -
        H = [-g for g in gifts]
        heapify(H)

        # for each second
        for _ in range(k):
            # pop the largest pile
            g = -heappop(H)

            # push the sqrt onto the heap
            heappush(H, -math.floor(math.sqrt(g)))

        return -sum(H)
