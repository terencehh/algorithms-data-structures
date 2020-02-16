#Merge Function which combines two sorted sequences and
# intertwines them together

def mergeSort(arr):

    # Space complexity we work with array of size n
    # and an addition O(log n) space to handle recursion
    # Hence O(N) auxiliary space

    if len(arr) > 1:
        mid = len(arr)//2 # Find the midpoint of array
        L = arr[:mid] # retrieve left half
        R = arr[mid:] # retrieve right half

        left_sorted = mergeSort(L)
        right_sorted = mergeSort(R)

        arr = merge(left_sorted,right_sorted)

    return arr

def merge(left, right):
    result = [] #result table
    i = j = 0 #counting variables

    left_len = len(left)-1
    right_len = len(right)-1

    while i <= left_len or j <= right_len: # make sure to retrieve all elements in left or right arrays
        
        if j > right_len or i <= left_len and left[i] <= right[j]: # if no more j elements or left index less than right index
            result.append(left[i])
            i += 1
        else:
            result.append(right[j]) # right index less than left index
            j += 1

    return result

print(mergeSort([12, 11, 13, 5, 6, 7]))
        
