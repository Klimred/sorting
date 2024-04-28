def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(1, i, 1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


# Quicksort implementation from
# https://www.geeksforgeeks.org/python-program-for-quicksort/
# using the first element as the pivot
def quicksort(arr):
    # if the array is empty or has only one element, no sorting is needed
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # put all elements smaller than the pivot in the
        # left array and all elements greater in the right array
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        # call quicksort recursively on the left
        # and right arrays and concatenate the results
        return quicksort(left) + [pivot] + quicksort(right)


# Merge sort implementation from https://www.programiz.com/dsa/merge-sort
def merge_sort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        l = array[:r]
        m = array[r:]

        # Sort the two halves
        merge_sort(l)
        merge_sort(m)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = m[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            array[k] = m[j]
            j += 1
            k += 1
