def find_max_palindrome_substring(s):
    largestPalindrome = ""
    currentPalindrome = ""
    
    if (len(s) != 1):
        for i in range(len(s)):
            # look at each character in the string
            # for each character, evaluate if we're looking
            # at a possible even length or odd length palindrome
            j = 0

            # check for even case by looking char to right of 'i'
            # for a match
            if (((i + 1) < len(s)) and
                (s[i] == s[i + 1])):
                j += 1

                while (((i - j) >= 0) and
                       ((i + 1) + j) < len(s)):
                    if (s[i -  j] != s[(i + 1) + j]):
                        break;

                    j += 1

            if (j > 0):
                # even length palindrome
                currentPalindrome = s[(i - j + 1):(i + 1 + j)]

            if (len(currentPalindrome) > len(largestPalindrome)):
                largestPalindrome = currentPalindrome

            j = 0

            # check for the odd case by looking at char to the
            # left and right of 'i'
            if (((i + 1) < len(s)) and
                ((i - 1) >= 0) and
                (s[i - 1] == s[i + 1])):
                j += 2

                while (((i - j) >= 0) and
                       ((i + j) < len(s))):
                    if (s[i -  j] != s[i + j]):
                        break;

                    j += 1

            # calculate palindrome
            if (j > 0):
                # odd length palindrome
                currentPalindrome = s[(i - j + 1):(i + j)]

            if (len(currentPalindrome) > len(largestPalindrome)):
                largestPalindrome = currentPalindrome
    else:
        largestPalindrome = s

    return largestPalindrome
