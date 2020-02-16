

def countingSort(array):

    #find the maximum integer
    max_num = max(array)
    # Create an empty array of size max_num
    count = [0] * (max_num + 1)

    # store number of occurences for each value into count array
    for value in array:
        count[value] += 1

    # Create an output sorted array
    sorted_array = []

    for i in range(1,len(count)):
        numOfOccurences = count[i]

        while numOfOccurences != 0:
            sorted_array.append(i)
            numOfOccurences -= 1

    return sorted_array

# print(countingSort([3,1,3,7,5,3,7,1]))
print(countingSort([3,1,3,7000,50,3,7,100])) # bad complexity