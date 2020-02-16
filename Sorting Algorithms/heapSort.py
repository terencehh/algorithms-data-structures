
  
# heapify subtree rooted at index i. 
# n is size of heap
# Takes O(log n) time
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[largest] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        print(arr) 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr)

    # Build a maxheap, takes O(n) time
    for i in range(n, -1, -1):
        heapify(arr, n, i)


    # One by one extract elements 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap

        print(arr)
        heapify(arr, i, 0)
        print(arr)
 
# heapSort has O(nlogn) for best,worst, and average case.
# Possible to have O(n) case for best case if equal keys
#The buildMaxHeap() operation is run once, and is O(n) in performance. The heapify function is O(log n), and is called n times. 
#Therefore, the performance of this algorithm is O(n + n log n) = O(n log n).
#Space complexity is O(1) Hence algorithm is in-place.

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra
