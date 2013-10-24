class LongestCommonSubstr(object):
    def genSubstrings(self, string):
        substrings = set()
        substringSize = len(string)

        # for each substring size, calc substring and add to result
        while (substringSize > 0):
            for substringStartIdx in range(substringSize):
                substring = string[substringStartIdx:substringSize]

                substrings.add(substring)

            substringSize -= 1

        #print("Answer: " + str(substrings))

        return substrings

    def calcLongestCommonSubstr(self, s1, s2):
        largestSubstring = ""
        
        ss1 = self.genSubstrings(s1)
        ss2 = self.genSubstrings(s2)

        # todo - can optimize if we start searching by the
        # longest substrings first; we would need to sort
        # each set and then start with picking strings
        # from the set of substrings corresponding to the
        # shorter of s1 and s2 (i.e., makes no sense to 
        # look for a 5 char string in s1's substrings if s1's
        # length is 3 chars)


        for s in ss1:
            if ((s in ss2) and 
                (len(s) > len(largestSubstring))):
                largestSubstring = s

        if (len(largestSubstring) == 0):
            return None

        return largestSubstring
