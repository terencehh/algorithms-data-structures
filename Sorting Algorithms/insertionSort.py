
def insertionSort(arr):

    for i in range(1, len(arr)):

        current_key = arr[i]
        j = i - 1

        while j >= 0 and current_key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current_key

        print(arr)
        
insertionSort([12, 11, 13, 5, 6])