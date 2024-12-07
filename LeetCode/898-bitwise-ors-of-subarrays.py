class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        Computes the number of unique bitwise-OR values
        created by OR'ing any contiguous subarray of `arr`

        Parameters
        ----------
        arr : list[int]
            array of numbers

        Returns
        -------
        m : int
            number of unique bitwise-OR values
        """
        # edge case, but need to check since might not be unique
        if len(arr) == 1:
            return 1

        # Initialize two sets - one for the allowable "starting" ORs (start)
        # and one for the aggregate unique ORs (agg).
        # The sets will automatically de-duplicate for us, which is nice
        start, agg = set(), set()

        # We basically want to keep track of the allowable "starting" ORs
        # For example, consider the subarrays ending at index `j`. The
        # XORs are:
        #    x[0] | x[1] | x[2] | ... x[j-1] | x[j]
        #           x[1] | x[2] | ... x[j-1] | x[j]
        #                  x[2] | ... x[j-1] | x[j]
        # so we basically need to start a new "chain" for every prior index
        for a in arr:
            # the "starting" ORs for the *next* iteration are
            # just the actual XORs ending at this value
            start = {a | s for s in start}
            start.add(a)  # add a chain to start at this value
            agg.update(start)  # all of `start` now end in `a`, so we can append these
        return len(agg)
