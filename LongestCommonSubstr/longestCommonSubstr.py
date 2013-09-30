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

        for s in ss1:
            if ((s in ss2) and 
                (len(s) > len(largestSubstring))):
                largestSubstring = s

        if (len(largestSubstring) == 0):
            return None

        return largestSubstring
