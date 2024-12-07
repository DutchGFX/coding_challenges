def isDecimalChar(c: str, no_zero: bool = False):
    """
    Determines if a string is a decimal digit using the ASCII code

    Parameters
    ----------
    c : str
        single character

    Returns
    -------
    isValid : bool
        TRUE if the character is 0-9
    """

    return (48 + no_zero) <= ord(c) <= 57


def stringToIntHelper(s: str, i: int, j: int, neg: bool):
    LIM = pow(2, 31) - 1 + neg  # maximum abs value

    # loop over all characters
    val = 0
    p = 0  # power
    for idx in range(j, i - 1, -1):  # right to left
        # get decimal value of character
        decVal = ord(s[idx]) - 48

        # if out of bounds
        if (LIM - val) < (add_to := decVal * pow(10, p)):
            return (1 - 2 * neg) * LIM

        val += add_to
        p += 1

    return (1 - 2 * neg) * val


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        neg = s.startswith("-")  # assume positive
        LIM = pow(2, 31) - 1 + neg  # maximum abs value

        if not s:
            return 0

        # this logic is sloppy but OK
        if s[0] in ["-", "+"]:
            s = s[1:]

        if (not s) or not isDecimalChar(s[0]):
            return 0

        # find first decimal non-zero character
        i = 0
        while i < len(s) and (not isDecimalChar(s[i])):
            i += 1

        # find index of the last decimal character in this block
        j = i
        while j < len(s) - 1 and isDecimalChar(s[j + 1]):
            j += 1

        # use the "helper" function
        return stringToIntHelper(s, i, j, neg)
