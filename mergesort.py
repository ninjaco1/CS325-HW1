import random
import numpy as np
def main():
    data = open("data.txt", "r")
    line = data.readlines()
    data.close()
    #print(line)
    array = []
    # loop through each line and sort and append each line into array
    for j in range(len(line)):
        temp = [int(i) for i in line[j].split() if i.isdigit()]
        mergesort(temp)
        array.append(temp)

    #print(array)

    #insert sorted data value in a different file
    out_file(array)

    # array = [1,5,2,6,9,0,8,3,7]
    # print (array)
    # # mergesort(array, 0, len(array)-1)
    # mergesort(array)
    # print (array)

def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        #divide
        mergesort(left)
        mergesort(right)

        i = j = 0 #left and right
        k = 0 # main array
        #conquer
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1


def out_file(array):
    out = open("output.txt", "w")
    out.truncate(0)
    for i in range(len(array)):
        write = ""
        for number in array[i]:
            write += str(number) + " "
        write += "\n"
        out.write(write)
    #print(write)
    out.close()

main()
