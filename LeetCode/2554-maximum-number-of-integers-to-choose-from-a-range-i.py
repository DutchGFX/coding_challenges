class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        """
        This is very simple. Of course we wish to accumulate the
        smallest integers possible. We sort and de-duplicate the list of
        banned numbers, then we simply add the smallest allowable integer
        until we hit `maxSum`

        Parameters
        ----------
        banned : list[int]
            banned integers. May contain dupliates. Not sorted.
        n : int
            maximum integer to use in the sum
        maxSum : int
            desied maximum sum

        Returns
        -------
        cnt : int
            maximum number of integers
        """
        # sort in ascending order and de-duplicate
        banned = sorted(list(set(banned)))

        # loop
        cnt = 0  # numbers we've used
        S = 0  # running sum
        for x in range(1, n + 1):
            # if this is in the band list, skip
            if banned and x == banned[0]:
                banned.pop(0)
                continue

            # add to the sum
            S += x

            # check if we have exceeded the sum. If not, increment cnt
            if S > maxSum:
                break
            cnt += 1
        return cnt
