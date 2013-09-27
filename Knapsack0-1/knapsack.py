class item(object):
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value


class knapsack(object):
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
        computedValues = [[0 for x in range(self.maxWeight)] for x in range(len(items))]

        # init the computed values for a knapsack w/ maximum weight support
        # of 0 and a knapsack w/ no items
        for i in range(self.maxWeight):
            pass

        return computedValues
