import math

def inject_char(char, listOfStrings):
    result = []

    for s in listOfStrings:
        for i in range(len(s) + 1):
            result.append(s[:i] + char + s[i:])

    return result

def permute(s):
    """ "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"] """
    # base case
    if (len(s) == 1):
        return [s]

    permutation = permute(s[1:])

    return inject_char(s[0], permutation)



s = "abcdefghi"
permutations = permute(s)
assert len(permutations) == math.factorial(len(s))
print(permute(s))
input("Done...")
