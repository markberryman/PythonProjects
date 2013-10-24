import math


def permute(prefix, string):
    # base case
    if (len(string) == 0):
        print(prefix)

    for i in range(len(string)):
        char = string[i]
        string_without_char = string[:i] + string[i+1:]
        permute(prefix + char, string_without_char)



s = "abc"
permutations = permute("", s)

input("Done...")
