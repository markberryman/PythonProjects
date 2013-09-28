class Item(object):
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value

    def __str__(self):
        return "Item {}, Weight {}, Value {}".format(self.id, self.weight, self.value)


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
        for row in range(len(computedValues)):
            for col in range(len(computedValues[0])):
                print(str(computedValues[row][col]) + " ", end="")

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
            for i in range(1, len(items) + 1):
                # since we range over values starting w/ index 1
                # we need to tweak the items array index reference
                item = items[i - 1]
                print("Looking at item: " + str(item))
                # and then for every possible knapsack capacity
                # calculate the total benefit of a specific combination of items
                for weight in range(self.maxWeight + 1):
                    print("Calc value for table location: [{}][{}]".format(i, weight))
                    # look at adding item to the knapsack
                    # if it's weight alone does not exceed the capacity of the
                    # knapsack, it can be part of a solution to the problem
                    if (item.weight <= weight):
                        print("Item's weight does *not* exceed current weight limit.")
                        # calculate the value of adding this item to a
                        # knapsack solution that does not contain this item
                        # and can accomodate the weight of this item

                        # need an index check here?
                        valueWithoutItemAndCapacityForCurrentItemsWeight = \
                            computedValues[i - 1][weight - item.weight]                        
                        print("Calculated value w/o item and item's weight: " + str(valueWithoutItemAndCapacityForCurrentItemsWeight))

                        valueWithoutItemAtCurrentWeight = \
                            computedValues[i - 1][weight]
                        print("Value w/o item at current weight: " + str(valueWithoutItemAtCurrentWeight))

                        valueWithItem = item.value + valueWithoutItemAndCapacityForCurrentItemsWeight
                        print("New calculated value w/ item: " + str(valueWithItem))

                        if (valueWithItem > valueWithoutItemAtCurrentWeight):
                            print("New calculated value with item is greater.")
                            # better to add the item; calculate the new value
                            computedValues[i][weight] = valueWithItem
                        else:
                            print("New calculated value with item is *not* greater.")
                            # better w/o adding the item; store that value instead
                            computedValues[i][weight] = valueWithoutItemAtCurrentWeight
                        
                    # else, if it's weight alone exceeds the capacity of
                    # the knapsack, store the benefit of the solution
                    # at the current knapsack capacity w/o item 'i'
                    else:
                        print("Item's weight does exceed current weight limit.")
                        if (i > 0):
                            computedValues[i][weight] = computedValues[i - 1][weight]
                        else:
                            # out of array bounds
                            computedValues[i][weight] = 0

                    self.print_values(computedValues)
                    
        return computedValues
