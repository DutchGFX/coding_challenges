class Solution:
    def isValid(self, s: str) -> bool:
        """
        Push open brackets to the stack and make sure they get closed
        before a different close happens
        """
        # array of OPEN characters, and dictionary of corresponding close characters
        OPEN_CHARS = ["(", "{", "["]  # all open characters
        CLOSE_OPEN_PAIRS = {")": "(", "}": "{", "]": "["}  # dictionary for indexing

        # loop over characters
        S = []
        for c in s:
            if c in OPEN_CHARS:
                S.append(c)
                continue
            elif (not S) or (S[-1] != CLOSE_OPEN_PAIRS[c]):
                return False
            S.pop(-1)
        return not len(S)
