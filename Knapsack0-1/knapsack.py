class Item(object):
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value


class Knapsack(object):
    """The Knapsack problem is a combinatorial optimization problem. Given
    a set of items w/ weights and values optimize the selection of items
    to maximize value w/o exceeding a specific weight.
    Brute force algorithm is exponential - O(2^n). Knapsack algorithm using
    dynamic programming technique is O(n * W) where n is the number of
    items to consider and W is the maximum weight.
    """
    def __init__(self, maxWeight):
        self.maxWeight = maxWeight
        
    def print_values(self, computedValues):
        for x in range(len(computedValues)):
            for y in range(self.maxWeight):
                print(str(computedValues[x][y]) + " ", end="")

            print("")

    def calculate_values(self, items):
        """Determine the value of each combination of items and store
        these values (solutions to a sub-problem) for future computations."""
        computedValues = None

        if ((self.maxWeight > 0) and (items is not None)):
            # all values set to 0 so no need to init values corresponding
            # to a knapsack w/ maximum weight support of 0 and a knapsack w/ 
            # no items
            computedValues = [
                [0 for x in range(self.maxWeight + 1)] 
                for x in range((len(items) + 1))
            ]

            # for every item
                # and then for every possible knapsack capacity, calculate
                # the total benefit of a specific combination of items
                    # look at adding item 'i' to the knapsack
                    # if it's weight alone does not exceed the capacity of the
                    # knapsack, it can be part of a solution to the problem
                        # calculate the benefit of adding this item to a
                        # knapsack solution that does not contain this item
                        # and can accomodate the weight of item 'i'
                        # if the new benefit including item 'i' is greater
                        # than the solution not including item 'i'
                        # store that benefit, else store the benefit of the
                        # solution w/o item 'i'

                    # else, if it's weight alone exceeds the capacity of
                    # the knapsack, store the benefit of the solution
                    # at the current knapsack capacity w/o item 'i'

        return computedValues
