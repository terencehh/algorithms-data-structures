
def partition(alist, first, last):

    pivot = alist[first]
    LBAD = first + 1
    RBAD = last - 1

    # continue until pointers cross
    while LBAD <= RBAD:

        # move LBAD right until it points to a bad element or crosses RBAD
        while LBAD <= RBAD and alist[LBAD] <= pivot:
            LBAD += 1

        # move RBAD left until it points to a bad element or crosses LBAD
        while LBAD <= RBAD and alist[RBAD] > pivot:
            RBAD -= 1

        # only swap if they have not crossed
        if LBAD <= RBAD:
            alist[LBAD],alist[RBAD] = alist[RBAD],alist[LBAD]
    
    # if crossed, swap element at RBAD with element at pivot
    alist[first],alist[RBAD] = alist[RBAD],alist[first]

    return RBAD # return pivot position after partitioning

def quickSort(alist, first, last):
    
    # sort only if the list contains at least two elements
    if (last - first) > 1:

        # partition the list from first to last (exclusive)
        print("partitioning", alist[first:last], "pivot", alist[first])

        # get the correct sorted position for the pivot
        # and place all elements <= pivot to left, > to right
        pivot_pos = partition(alist,first,last)

        print("partitioned:", alist[first:last])

        #recursively sort the two halves of the list
        print("Splitting into two", alist[first:pivot_pos], alist[pivot_pos+1:last])
        quickSort(alist, first, pivot_pos)
        quickSort(alist, pivot_pos+1, last)

alist = [26,93,44,20,77,31,36,28,55,17]
quickSort(alist,0,len(alist))
print(alist)
