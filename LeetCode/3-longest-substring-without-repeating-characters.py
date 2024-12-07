class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Compute the length of the longest substring without repeated characters

        We start at left=0 and right=0 and increment
        right until we get a duplicate character
        Then we increment left until we pass that character, and repeat the process

        Parameters
        ----------
        s : str
            string

        Returns
        -------
        cnt : int
            maximum substring length with no repeated characters
        """
        left = 0
        right = 0
        cnt = 0
        maxcnt = 0
        while right < len(s):
            if s[right] not in s[left:right]:
                cnt = right - left + 1
                right += 1
            else:
                # increment left until s[right] isn't in the substring
                left += 1

            maxcnt = max(cnt, maxcnt)
        return maxcnt
