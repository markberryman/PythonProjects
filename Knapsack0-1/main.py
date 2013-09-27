import knapsack

ks = knapsack.Knapsack(5)
item1 = knapsack.Item(1, 2, 3)
item2 = knapsack.Item(2, 3, 4)
item3 = knapsack.Item(3, 4, 5)
item4 = knapsack.Item(4, 5, 6)
x = ks.calculate_values([item1, item2, item3, item4])
ks.print_values(x)

input('Press Enter to exit')
