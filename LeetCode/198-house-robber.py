class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Determines the maximum loot we can obtain given that
        we cannot rob adjacent houses

        Parameters
        ----------
        nums : list[int]
            loot at each house

        Returns
        -------
        m : int
            maximum loot

        Notes
        -----
        - At each house, we can decide to either rob or not rob the house
        - If we decide to rob the house, we collect the loot from the current
          house, plus the loot we would have collected if we did NOT rob the
          previous house. This is because we know that if we rob this house,
          we must not have robbed the previous house.
        - If we do not rob this house, we can collect either the loot we
          collected from robbing the previous house, OR the loot we collected
          by not robbing the previous house, whichever is higher.
        - After we update the two running totals, we can make our decision
          based on which value (robbing or not robbing this house) produces
          more loot.
        """
        sum_robbed_last = 0  # if we robbed the last house
        sum_did_not_rob = 0  # if we did not rob the house
        for n in nums:
            # update the (temporary) total for if we don't rob this house
            # If we don't rob the house, we can collect either the
            # total for robbing or not robbing the previous house
            sum_did_not_rob_tmp = max(sum_robbed_last, sum_did_not_rob)

            # update the total if we rob this house
            # If we rob this house, we must not have robbed the previous house
            sum_robbed_last = sum_did_not_rob + n

            # update the max and update "did_not_rob" total using the temp variable
            sum_did_not_rob = sum_did_not_rob_tmp
            m = max(sum_robbed_last, sum_did_not_rob)

        return m
