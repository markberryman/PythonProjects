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
