def bottom_up_min_coin_change_problem(coin_list, value):
    # this is bottom up solution
    # time complexity: O(NV)
    # space complexity: O(V + N)

    # construct memo from 1 until V
    memo = [0] * (value + 1)
    for i in range(1, len(memo)):
        min_coin = float('inf')  # set default large value
        for coin in coin_list:
            if coin <= value:
                c = 1 + memo[value - coin]
                if c < min_coin:
                    min_coin = c
        memo[i] = min_coin

    return memo[value]


def top_down_min_coin_change_problem(coin_list, value):
    # recursively call top down until reach the starting index, then build
    # memoization table up

    if coin_memo[value] != -1:
        return coin_memo[value]
    else:
        min_coins = float('inf')
        for coin in top_down_coin_list:
            if coin <= value:
                c = 1 + top_down_min_coin_change_problem(coin_list, value - coin)
                if c < min_coins:
                    min_coins = c

        coin_memo[value] = min_coins
        return coin_memo[value]


top_down_coin_list = [9, 5, 6, 1]
value = 15
coin_memo = [-1] * (value + 1)
coin_memo[0] = 0

print(bottom_up_min_coin_change_problem([9, 5, 6, 1], 11))
