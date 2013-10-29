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
                # even length palindrome case
                currentPalindrome = s[(i - j + 1):(i + 1 + j)]
    
            if (len(currentPalindrome) > len(largestPalindrome)):
                largestPalindrome = currentPalindrome
    else:
        largestPalindrome = s

    return largestPalindrome

#string maxPalindrome;
#string curPalindrome;

#for (var i = 0; i > 0; i++) {
#  // assume all palindromes are odd size
#  // for a given position in the string 'i', check for 
#  // matches of chars b/w i - 1 and i + 1, until
#  // i < 0 or i > s.Length
#  int j = 0;
#  bool evenCase = True;

#  // determine if we have an even or odd palindrome case
  
#  // check for even case by looking at next char
#  if (s[i+1] == s[i]) {
#    for ((i - j > 0) and (((i + 1) + j) < s.Length); j++) {
#        if (s[i - j] != s[(i + 1) + j]) {
#            break;
#        }
#  } else {
#      oddCase = True;
#      // check for odd case by looking at char before and after current char
#      for ((i - j > 0) and (i + j < s.Length); j++) {
#        if (s[i - j] != s[i + j]) {
#          break;
#        }

#  if (j > 0) {
#    if (evenCase) {
#      // 2nd param to substring fn is length
#      curPalindrome = s.substring(i - j + 1, j * 2);
#    } else {      
#      curPalindrome = s.substring(i - j + 1, (j * 2) + 1);
#    }
    
#    if (curPalindrome.Length > maxPalindrome.Length) {
#      maxPalindrome = curPalindrome;
#    }  
#  }
#}

#return maxPalindrome;

