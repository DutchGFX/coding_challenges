class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            j = len(s)
            for i, c in enumerate(s):
                if (i > len(prefix) - 1) or (prefix[i] != c):
                    j = i
                    break
            prefix = prefix[:j]
        return prefix
