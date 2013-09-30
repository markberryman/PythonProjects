class Item(object):
    def __init__(self, id, weight, benefit):
        self.id = id
        self.weight = weight
        self.benefit = benefit

    def __str__(self):
        return "Item {}, Weight {}, Benefit {}".format(self.id, self.weight, self.benefit)


class Knapsack(object):
    """The Knapsack problem is a combinatorial optimization problem. Given
    a set of items w/ weights and values optimize the selection of items
    to maximize value w/o exceeding a specific weight.
    Brute force algorithm is exponential - O(2^n). Knapsack algorithm using
    dynamic programming technique is O(n * W) where n is the number of
    items to consider and W is the maximum weight.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        
    def print_values(self, computedValues):
        for row in range(len(computedValues)):
            for col in range(len(computedValues[0])):
                print(str(computedValues[row][col]) + " ", end="")

            print("")

    def calculate_benefits(self, items):
        """Determine the value of each combination of items and store
        these values (solutions to a sub-problem) for future computations."""
        benefitsTable = None

        if ((self.capacity > 0) and (items is not None)):
            # creating a table with 0..# items rows and 0..knapsack capacity
            benefitsTable = [
                [0 for x in range(self.capacity + 1)] 
                for x in range((len(items) + 1))
            ]

            # start at index 1 b/c we need a base row of 0's for
            # the calculations
            # for each item
            for i in range(1, len(items) + 1):
                # the items array is 0 based so we tweak the
                # list index reference
                item = items[i - 1]
                print("Looking at item: " + str(item))
                # for every possible knapsack capacity
                # calculate the total benefit of a combination of items
                for capacity in range(self.capacity + 1):
                    print("Calc value for table location: [{}][{}]".format(i, capacity))
                    # add item to knapsack?
                    # if item's weight < less than knapsack capacity,
                    # it can be part of a solution
                    # this check also prevents any index out of bounds
                    # calculations down the road b/c we'll never have
                    # an item w/ a weight that could result in a < 0 index calc                    
                    if (item.weight <= capacity):
                        print("Item's weight does *not* exceed current weight limit.")
                        # calc value of solution w/ this item plus a knapsack
                        # solution that does not contain this item that could
                        # take this item's weight
                        valueWithoutItemAndCapacityForItemsWeight = \
                            benefitsTable[i - 1][capacity - item.weight]                        
                        print("Calculated value w/o item and item's weight: " + str(valueWithoutItemAndCapacityForItemsWeight))

                        valueWithoutItemAtCurrentCapacity = \
                            benefitsTable[i - 1][capacity]
                        print("Value w/o item at current capacity: " + str(valueWithoutItemAtCurrentCapacity))

                        valueWithItem = item.benefit + valueWithoutItemAndCapacityForItemsWeight
                        print("New calculated value w/ item: " + str(valueWithItem))

                        if (valueWithItem > valueWithoutItemAtCurrentCapacity):
                            print("New calculated value with item is greater.")
                            # better to add the item; calculate the new value
                            benefitsTable[i][capacity] = valueWithItem
                        else:
                            print("New calculated value with item is *not* greater.")
                            # better w/o adding the item; store that value instead
                            benefitsTable[i][capacity] = valueWithoutItemAtCurrentCapacity
                        
                    # else, if item's weight > knapsack capacity,
                    # it can't be part of a solution
                    # store the previously calculated benefit of a 
                    # knapsack w/ the same capacity and w/o this item
                    else:
                        print("Item's weight does exceed current weight limit.")
                        if (i > 0):
                            benefitsTable[i][capacity] = benefitsTable[i - 1][capacity]
                        else:
                            # out of array bounds
                            benefitsTable[i][capacity] = 0

                    self.print_values(benefitsTable)
                    
        return benefitsTable

    def find_items(self, items, benefitsTable):
        """To determine the items that make up the maximum value, we need
        to walk back through the array of computed values comparing
        calculated values for a given item and the knapsack w/o that item.
        If there's a benefit difference, then the item is part of the
        optimal computed value. If not, it isn't."""
        numItems = len(items)
        curCapacity = self.capacity
        knapsackItems = []

        while ((numItems > 0) and (curCapacity > 0)):
            if (benefitsTable[numItems][curCapacity] != benefitsTable[numItems - 1][curCapacity]):
                knapsackItems.append(items[numItems - 1])
                numItems -= 1
                curCapacity -= items[numItems].weight
            else:
                numItems -= 1

        return knapsackItems