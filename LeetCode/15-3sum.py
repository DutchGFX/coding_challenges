class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        inds = []
        d = sorted(nums)  # sort the array
        for a in range(len(d) - 2):  # loop over all allowable index a
            # the *smallest* possible sum when starting at `a` is `(a, a+1, a+2)`
            # so we start with `b=a+1`, which gives us the smallest two-element sum
            b = a + 1  # the value just to the right

            # then we find the largest `c` value that satisfies the criteria
            c = len(d) - 1  # start at the opposite end
            while b < c:  # we know b < c
                s = d[a] + d[b] + d[c]  # compute the sum
                if s < 0:  # too small; increment b to get a larger sum
                    b += 1
                    continue
                if s == 0:  # satisfies the criteria; append
                    inds.append((d[a], d[b], d[c]))

                # decrement c to get a smaller (or equal) sum
                c -= 1
        # de-duplicate before appending
        inds = list(set(inds))
        return inds
