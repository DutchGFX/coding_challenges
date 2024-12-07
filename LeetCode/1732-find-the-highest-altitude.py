class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """
        Finds the highest altitude point

        Parameters
        ----------
        gain : list[int]
            difference in altitude from point `[i]` to point `[i+1]`

        Returns
        -------
        m : int
            maximum elevation
        """
        m = -1e14  # initialize max
        alt = 0  # current altitude. Value does not matter
        for g in gain:  # for every gain
            alt += g  # add the gain to get the current altitude
            m = max(alt, m)  # take the max to see if it's the new max
        return m
