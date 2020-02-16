



def bottom_up_unbounded_knapsack(capacity, set_of_items):
    #seperate weights and values
    weights = []
    values = []
    num_of_items = len(set_of_items)

    for i in range(len(set_of_items)):
        weights.append(set_of_items[i][0])
        values.append(set_of_items[i][1])

    # initialize memo list to store max values at each capacity
    memo = [0] * (capacity+1)

    for i in range(capacity+1):
        maxValue = 0
        for c in range(num_of_items):     
            # if the current weight of bag is
            # less than weight of index
            if weights[c] <= i:
                thisValue = values[c] + memo[i - weights[c]]

                if thisValue > maxValue:
                    maxValue = thisValue
        memo[i] = maxValue

    return memo[capacity]

weights = [9,5,6,1]
values = [550,350,180,40]
capacity = 12
memo = [-1] * (capacity+1)  # initialize memo list to store max values at each capacity
memo[0] = 0
def top_down_unbounded_knapsack(capacity):
    # top_down requires memo to already be set up

    if memo[capacity] != -1:
        return memo[capacity]
    else:
        maxValue = 0
        for i in range(len(values)): # can also be weights / doesnt matter
            if weights[i] <= capacity:
                thisValue = values[i] + top_down_unbounded_knapsack(capacity - weights[i])
                if thisValue > maxValue:
                    maxValue = thisValue

        memo[capacity] = maxValue
        return memo[capacity]

def zero_one_knapsack(capacity, set_of_items):
    # Same as unbounded except each item can only be picked at most once
        #seperate weights and values
    weights = []
    values = []
    coin_length = len(set_of_items)

    for i in range(coin_length):
        weights.append(set_of_items[i][0])
        values.append(set_of_items[i][1])





# def edit_distance_problem(s1, s2):
#     return False
#     # if the last character of each string is same where
#     # s1[n] == s2[m] 
#     # then just compute s1[1..n-1] and s2[1..m-1]


#     # if want to substitue last string
#     # cost is 1 + calling function s1[1..n-1] and s2[1..m-1]

#     if s1[n] == s2[m]:
#         cost = edit_distance_problem(s1[1..n-1],s2[1..m-1])

#     else:
#         # take the minimum cost of 3 possible operations

#         # if substituting s1[n] with s2[m]


        
#         # if adding s2[m] in s1 after s1[n]

#         # if removing s1[n]


def lcs(string1,string2):
    # make sure the larger string is in x
    # this is important for backtracking
    if len(string1) >= len(string2):
        X = string1
        Y = string2
    else:
        X = string2
        Y = string1
    
    lengthX = len(X) + 1
    lengthY = len(Y) + 1

    # Construct 2D table of characters of 2 strings
    memo = [ [0] * lengthY for i in range(lengthX) ]

    for i in range(1,lengthX):

        for j in range(1,lengthY):

                # if the characters do not match
                # then the problem will be the same as either:
                # 1. X[0..i-1] & Y[0..j] = take 1 character less of string X
                # 2. X[i] & Y[0..j-1] = take 1 character less of string Y
                # we retrieve the max value of the longest common substring between the two
            if X[i-1] != Y[j-1]:
                memo[i][j] = max(memo[i-1][j],memo[i][j-1])

                # if the characters match
                # then the value will be 1 + the substring of the
                # two strings before it (X[0..i-1] & Y[0..j-1] )
            if X[i-1] == Y[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]

    x_length = len(X)
    y_length = len(Y)
    print("Longest Common Substring is of length: ", memo[x_length][y_length])
    print("Backtracking to find LCS now...")
    lcs_string = ""

    while x_length > 0 and y_length > 0:

        left_cell = memo[x_length-1][y_length]
        top_cell = memo[x_length][y_length-1]

         # If current value in both strings are the same, add
        # it to our decoded message
        if X[x_length-1] == Y[y_length-1]:
            lcs_string += X[x_length-1]
            x_length -= 1
            y_length -= 1

            # if do not match we find the max lcs value between
            # string x[0..x_length-1] or y[0..y_length-1]
        elif left_cell > top_cell:
            x_length -= 1
        else:
            y_length -= 1            
            
    lcs_string = lcs_string[::-1]
    return lcs_string
      

def main():

    # Top-down approach start by attempting the largest problem first
    # bottom-up approach start by attempting the smallest problem first
    # Note: All top-down solutions require setup before calling function

    # print(bottom_up_fib(fib_num))
    # print(top_down_fib(fib_num,top_down_table))

    # print(bottom_up_min_coin_change_problem([9,5,6,1],15))
    # print(top_down_min_coin_change_problem(top_down_coin_list,value))

    # print(bottom_up_unbounded_knapsack(12, [[9,550],[5,350],[6,180],[1,40]] ))
    # print(top_down_unbounded_knapsack(capacity))
    print(zero_one_knapsack(11, [[6,230],[1,40],[5,350],[9,550]] ))

    # print(lcs("bdceMlonfashxzunivyeriasityb", "MondcaitjshukniveptnQrsiXteyY"))




if __name__ == "__main__":
    main()
