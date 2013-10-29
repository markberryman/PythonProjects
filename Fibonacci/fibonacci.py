def fib(nth_num):
    """0, 1, 1, 2, 3, 5, 8, ..."""
    result = None

    if (nth_num == 1):
        return 0

    prev_prev_num = 0
    prev_num = 1

    while (nth_num > 1):
        result = prev_num + prev_prev_num

        prev_prev_num = prev_num
        prev_num = result

        nth_num -= 1

    return result

n = 10

while (n > 0):
    print(fib(n))
    n -= 1

input("Enter to exit.")