class StringProblems(object):
    @staticmethod
    def remove_dupes(s):
        """No additional space beyond a few small tracking vars.
        Minimal number of operations to "compact" the array."""
        # can't have dupes if string only one char; special case
        if ((s is None) or (len(s) < 2)):
            return s

        tail = 0    # tracks last position of a unique character

        # we'll look at each character except the first; no need
        for i in range(1, len(s)):
            for j in range(i + 1):
                # we'll look at all characters before that character
                if (s[i] == s[j]):
                    # dupe char
                    break

            if (j == i):
                # unique char
                tail += 1
                s[tail] = s[i]

        # we're done checking characters
        # drop everything after the tail
        # since we can't drop a null terminator to
        # designate the end of the string, we'll have
        # to create a new string
        return s[:tail + 1]

    @staticmethod
    def reverse_string(s):
        """Reverse string in place."""
        startIdx = 0
        endIdx = len(s) - 1

        while (endIdx > startIdx):
            temp = s[startIdx]
            s[startIdx] = s[endIdx]
            s[endIdx] = temp

            startIdx += 1
            endIdx -= 1

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