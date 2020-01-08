import random
import numpy as np
def main():
    list = np.random.randint(0,200,10)
    print list
    mergesort(list, 0, len(list)-1)
    print list

def merge(array, left, middle, right):
    left_elements = middle - left + 1
    right_elements = right - middle

    # creating a temp array with 0s in it
    Left = [0] * left_elements
    Right = [0] * right_elements

    # copy data over to temp arrays
    for i in range(left_elements):
        Left[i] = array[left + i]

    for j in range(right_elements):
        Right[j] = array[middle + 1 + j]


    # merge the arrays together
    i = j = 0 # index of left and right subarrays
    k = left # index of merged subarray

    while i < left_elements and j < right_elements:
        if Left[i] <= Right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = Right[j]
            j += 1
        k += 1

    while i < left_elements:
        array[k] = Left[i]
        i += 1
        k += 1

    while j < right_elements:
        array[k] = Right[j]
        j += 1
        k += 1

def mergesort(array, left, right):
    if left < right:
        #call left and right arrays
        #half = len(array)//2 # // means floor divide
        #left = array[:len(array)//2]
        #right = array[len(array)//2:]
        middle = (left + right -1)/2
        mergesort(array, left, middle) # left
        mergesort(array, middle +1, right) # right
        merge(array, left, middle, right)

main()
