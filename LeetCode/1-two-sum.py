class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of the two numbers that sum to `target`

        Parameters
        ----------
        nums : list[int]
            numbers
        target : int
            integer sum target

        Returns
        -------
        inds : tuple
            indices

        Notes
        -----
        We could obviously brute force with O(N^2) but that's boring.
        Instead, we sort the array (O(n*log(n)) and then use a two-pointers
        approach. We sort the array (including the original indices, of course),
        and then we start by taking the smallest and largest value. For a given
        smaller value, `i`, the largest sum we can get is by using the end of the sorted
        array. If that value is too small, we need to increase `i`. If that value is too big,
        we decrease `j`, since we don't need to increase `i` since we already started at `i=0`.
        Basically, we start with the "widest" array and slowly narrow each edge until we find the
        target.
        """

        tups = [(n, idx) for idx, n in enumerate(nums)]
        tups.sort()
        i = 0  # initial leftmost index
        j = len(tups) - 1  # initial rightmost index
        while i < j:
            # compute the sum
            s = tups[i][0] + tups[j][0]

            # check
            if s == target:
                print(tups[i], tups[j])
                return tups[i][1], tups[j][1]
            elif s > target:  # shrink the right side
                j -= 1
            else:  # shrink the left side
                i += 1
