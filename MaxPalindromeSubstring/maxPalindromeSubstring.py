def find_palindrome_from_center(s, left_idx, right_idx):
    # the two indices could be one apart or the same value
    # regardless, we expand equally going left and right
    # to calculate the size of the palindrome from the
    # given point(s)
    while ((left_idx >= 0) and
           (right_idx < len(s))):
        if (s[left_idx] == s[right_idx]):
            # expand the search
            left_idx -= 1
            right_idx += 1
        else:
            break

    return s[left_idx + 1:right_idx]

def find_max_palindrome_substring(s):
    largestPalindrome = ""
    
    if (len(s) != 1):
        for i in range(len(s)):
            # look at each character in the string
            # for each character, evaluate if we're looking
            # at a possible even length or odd length palindrome

            # even case
            evenPalindrome = find_palindrome_from_center(s, i, i + 1)
            oddPalindrome = find_palindrome_from_center(s, i, i)

            if ((len(evenPalindrome) > len(oddPalindrome)) and
                (len(evenPalindrome) > len(largestPalindrome))):
                largestPalindrome = evenPalindrome

            if ((len(oddPalindrome) > len(evenPalindrome)) and
                (len(oddPalindrome) > len(largestPalindrome))):
                largestPalindrome = oddPalindrome
    else:
        largestPalindrome = s

    return largestPalindrome
