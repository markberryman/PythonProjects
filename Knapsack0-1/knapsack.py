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

            # for every item (can skip the 0 index)
            # TODO - skip the zero index; same for weight check
            for itemIdx in range(len(items)):
                item = items[itemIdx]
                # and then for every possible knapsack capacity
                # calculate the total benefit of a specific combination of items
                for weight in range(self.maxWeight):
                    # look at adding item to the knapsack
                    # if it's weight alone does not exceed the capacity of the
                    # knapsack, it can be part of a solution to the problem
                    if (item.weight <= weight):
                        # calculate the value of adding this item to a
                        # knapsack solution that does not contain this item
                        # and can accomodate the weight of this item

                        # need an index check here?
                        valueWithoutItemAndCapacityForCurrentItemsWeight = \
                            computedValues[itemIdx - 1][weight - item.weight]
                        valueWithoutItemAtCurrentWeight = \
                            computedValues[itemIdx - 1][weight]
                        valueWithItem = item.value + valueWithoutItemAndCapacityForCurrentItemsWeight

                        if (valueWithItem > valueWithoutItemAtCurrentWeight):
                            # better to add the item; calculate the new value
                            computedValues[itemIdx][weight] = valueWithItem
                        else:
                            # better w/o adding the item; store that value instead
                            computedValues[itemIdx][weight] = valueWithoutItemAtCurrentWeight
                        
                    # else, if it's weight alone exceeds the capacity of
                    # the knapsack, store the benefit of the solution
                    # at the current knapsack capacity w/o item 'i'
                    else:
                        if (itemIdx > 0):
                            computedValues[itemIdx][weight] = computedValues[itemIdx - 1][weight]
                        else:
                            # out of array bounds
                            computedValues[itemIdx][weight] = 0
                    
        return computedValues
