# given a list of items, determine if one of them is the
# "best candidate" which means it's better than all other
# items in the list; a "better than" function does the
# comparison

# a brute force solution would be to take each item in the
# list and compare it to all others; if that item was
# better than all others, it would be the best candidate
# but, there's a better approach; instead, we can start
# w/ the first item, compare it to the second and if it's
# better than the 2nd item, move on to the 3rd item; if it's
# not better than the 2nd item, the 2nd item b/c our
# "best candidate" and we continue comparisons
# at the end of the comparisons, we know two things:
# 1. the current "best candidate" has not lost a comparison
# 2. all other items have lost at least one comparison so
#    none of them can be the best candidate
# the last test though is to take our current "best candidate"
# and recompare it to all other items in the list since
# the concept of "better than" is not transitive
# (i.e., A can be better than B, B can be better than C,
# but A might not be better than C)


def better_than(item1, item2):
    # "a" beats "b"
    if ((item1 == "a") and (item2 == "b")):
        return True

    # "c" beats "a"
    if ((item1 == "c") and (item2 == "a")):
        return True

    # "b" beats "c"
    if ((item1 == "b") and (item2 == "c")):
        return True

    # "d" beats all
    if (item1 == "d"):
        return True
    if (item2 == "d"):
        return False

    if (item1 == item2):
        return True
    
def best_candidate(data):
    curBC = data[0]

    for i in range(1, len(data)):
        if (better_than(data[i], curBC)):
            curBC = data[i]

    for i in range(len(data)):
        if (not better_than(curBC, data[i])):
            return None

    return curBC

data = ["a", "b", "c"]          # no best candidate
#data = ["a", "b", "c", "d"]     # "d" is best candidate
result = best_candidate(data)

if (result is None):
    print("No best candidate.")
else:
    print(result)

input()