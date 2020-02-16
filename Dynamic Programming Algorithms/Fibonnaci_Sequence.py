
def top_down_fib(n, table):
    if n == 0 or n == 1:
        table[n] = n

    # If value not calculated, then calculate it

    if table[n] is None:
        table[n] = top_down_fib(n - 1, table) + top_down_fib(n - 2, table)

    # return the value corresponding to the value of n
    return table[n]


def bottom_up_fib(N):
    # Time complexity: 2*N times, so O(N)

    memo = [0] * (N + 1)

    endpoint = len(memo)
    memo[0] = 0
    memo[1] = 1

    for i in range(2, endpoint):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[endpoint - 1]


fib_num = 10
top_down_table = [None] * (fib_num + 1)