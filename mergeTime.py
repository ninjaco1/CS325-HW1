from random import seed
from random import randint
import numpy as np
import time


def main():
    run_time = []
    for i in range(1000,31000,3000):
        array = []
        sum = 0
        temp_runtime =[]
        for j in range(i):
            array.append(randint(0,10000))
        for k in range(3): # run 3 times then average
            temp = array.copy()
            #print(array)
            start_time = time.time()
            mergesort(temp)
            end_time = time.time() - start_time
            temp_runtime.append(end_time)
            #print(end_time)
            sum += end_time
            #temp.clear()

        temp_runtime.append(sum/3)
        print(temp_runtime)
        string = ""
        for number in temp_runtime:
            string += str(number) + " "
        string += "\n"
        #print(string)
        run_time.append(string)
        array.clear()
        temp_runtime.clear()
    #print(run_time)
    runtime_file(run_time)

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


def runtime_file(runtime):
    file = open("mergetime.txt","w")
    file.truncate(0)
    for string in runtime:
        file.write(string)
    file.close()

main()
