
def selectionSort(arr):

    for i in range(len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

print(selectionSort([2, 4, 6, 5, 8]))