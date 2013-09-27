import knapsack

ks = knapsack.Knapsack(3)
x = ks.calculate_values([(1,1),(2,2)])
ks.print_values(x)

input('Press Enter to exit')
