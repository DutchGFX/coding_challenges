class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Computes the product of every array element except the index itself

        Parameters
        ----------
        nums : list[int]
            numbers

        Returns
        -------
        L : list[int]
            products

        Notes
        -----
        - We use pre- and post-product arrays
        - `prefixes[i] = nums[0] * nums[1] ... * nums[i-1]`
        - `suffixes[i] = nums[i+1] * nums[i+2] ... * nums[-1]`
        """
        N = len(nums)
        prefixes = [1] * N
        suffixes = [1] * N
        for i in range(N - 1):
            prefixes[i + 1] = prefixes[i] * nums[i]
            suffixes[-i - 2] = suffixes[-i - 1] * nums[-i - 1]
        L = [p * s for p, s in zip(prefixes, suffixes)]
        return L
