from heapq import heapify, heappush, heappop


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        """
        Given a list of events, find the maximum "value" that can
        be obtained by attending at most 2 non-overlapping events

        Parameters
        ----------
        events : list[list[int]]
            events where `events[i] = [startTime, endTime, value]`
            The times are inclusive

        Returns
        -------
        m : int
            maximum value

        Notes
        -----
        - We only need to select 2 intervals, so this isn't so hard.
        - We can start with any of the intervals. WLOG, we'll use that as the
          leftmost interval. We then find the maximum of the intervals to the right, and
          that gives us our sum.
        - We use a MaxHeap (by negating the values and feeding them to a MinHeap) to
          maintain the intervals to the right, since we sorted by end time
        - We pop items off the stack until the start is greater than the end time
        """

        # feed into maxheap by negating the value
        # since Python's default is a minheap
        H = []  # maxheap where each event is (-value, tStart, tEnd)
        for e in events:
            e[2] *= -1  # negate for use in MaxHeap
            heappush(H, (e[2], e[0], e[1]))  # push to the heap

        # sort the events by end time
        events.sort(key=lambda e: e[1])

        # loop over events sorted by end time
        m = 1e14
        for _, t_end, val in events:
            while H and H[0][1] <= t_end:
                heappop(H)
            val += H[0][0] if H else 0
            m = min(val, m)
        return -m
