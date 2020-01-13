import random
import numpy as np
def main():
    #array = np.random.randint(0,200,10)
    #print (array)
    # mergesort(array, 0, len(array)-1)
    data = open("data.txt", "r")
    line = data.readlines()
    data.close()
    #print(line)
    array = []
    for j in range(len(line)):
        temp = [int(i) for i in line[j].split() if i.isdigit()]
        print(temp)
        insertionsort(temp)
        array.append(temp)

    #print(array)
    #insertionsort(array)
    out_file(array)

def insertionsort(array):
    # bubble sort
    # for i in range(1,len(array)):
    #     for j in range(i,0,-1):
    #         if array[j] <= array[j-1]:
    #             array[j], array[j-1] = array[j-1], array[j]
    #insertion sort
    for i in range(1, len(array)):
        current = i
        while(array[i] <= array[current-1]):
            current -= 1
            if(current==0):
                break
        array.insert(current, array[i])
        array.pop(i+1)

    #print(array)

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
