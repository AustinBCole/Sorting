# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # We dont iterate over the last index because the nested loop starts at i + 1, so if we were to be at the last index we would get an `index out of range` error.
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        
        swapped_value = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = swapped_value
    print(arr)
    return arr

selection_sort([0,5,2,3,1])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print(True)
            swapped_value = arr[i]
            arr [i] = arr[i + 1]
            arr[i + 1] = swapped_value
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
