class StringProblems(object):
    @staticmethod
    def is_all_unique_chars(s):
        """This works if we know all chars are in the extended ASCII
        character set. Uses a small amount of add'l space but O(n)."""
        charTrack = [0] * 256

        for i in range(len(s)):
            ordVal = ord(s[i])

            if (charTrack[ordVal] != 0):
                return False

            charTrack[ordVal] = 1

        return True

    #@staticmethod
    #def is_all_unique_chars(s):
    #    """Not using a separate data structure so no extra
    #    space used but this is O(n^2)."""
    #    for i in range(len(s)):
    #        for j in range(i + 1, len(s)):
    #            if (s[i] == s[j]):
    #                return False

    #    return True