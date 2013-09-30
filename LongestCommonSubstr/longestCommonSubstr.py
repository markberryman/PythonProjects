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

    def calcLongestCommonSubstr(self, substrings1, substrings2):
        pass
