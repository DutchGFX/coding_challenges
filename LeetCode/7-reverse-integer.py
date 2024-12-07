import math


class Solution:
    def reverse(self, x: int) -> int:
        """
        We basically "bit shift" by dividing by 10 to find the coefficient of the highest
        power of 10 (call it the MSD, most significant digit).
        We then insert that into our new integer as the LSD, and then remove the MSD
        from `x` by shifting it back up (mutliplying by 10^p) and subtracting from `x`.
        """

        # edge case
        if x == 0:
            return 0

        # compute the limit, take abs
        neg = x < 0
        LIM = pow(2, 31) - 1 + neg  # 2^31 if neg, 2^31 - 1 if pos
        x = abs(x)  # always make it positive for reversing

        # find highest power of 10
        max_pow = int(math.floor(math.log10(abs(x))))
        new = int(0)
        for p in range(max_pow, -1, -1):  # start at highest power
            # extract the coeff of 10^p
            tmp = x // pow(10, p)

            # if we are going out-of-bounds
            # we could probaby
            to_add = tmp * pow(10, max_pow - p)
            if to_add > LIM - new:
                return 0

            # add it as the coeff of 10^(max-p)
            new += to_add

            # remove it from x
            x -= tmp * pow(10, p)

        new = -new if neg else new
        return new
