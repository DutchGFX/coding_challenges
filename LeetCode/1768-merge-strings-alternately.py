class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges strings alternately

        Parameters
        ----------
        word1, word2 : str
            the two strings to be merged
        
        Returns
        -------
        s : str
            merged string
        """
        s = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                s += word1[i]
            if i < len(word2):
                s += word2[i]
        return s
