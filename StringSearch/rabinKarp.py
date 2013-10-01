class RabinKarp(object):
    """String search algo using a rolling hash approach."""

    def ascii_sum_hash_fn(self, string):
        sum = 0

        for char in string:
            sum += ord(char)

        return sum

    def ascii_sum_rolling_hash(self, lastString, lastHash, string):
        """Quick b/c we're using previously computed hash values."""
        result = 0

        if ((lastString is not None) and
            (len(string) > 1)):
            # new hash equals last hash minus hash value of first char
            # plus hash value of last char in string
            # lastString = "abc"
            # string = "bcd"
            result = \
                lastHash - \
                self.ascii_sum_hash_fn(lastString[0]) + \
                self.ascii_sum_hash_fn(string[len(string) - 1])
        else:
            result = self.ascii_sum_hash_fn(string)

        return result

    def contains_string(self, s1, s2):
        """Returns bool indicating if s1 in s2."""
        result = False

        s1Hash = self.ascii_sum_hash_fn(s1)
        lastSubstring = None
        lastHash = 0

        # go over each substring in s2 of size equal to length of s1
        for x in range(len(s2) - len(s1) + 1):
            substring = s2[x:x + len(s1)]
            substringHash = self.ascii_sum_rolling_hash(lastSubstring, lastHash, substring)

            if (substringHash == s1Hash):
                # match?
                if (s1 == substring):
                    result = True
                    break

            # no match :-(
            lastSubstring = substring
            lastHash = substringHash

        return result
