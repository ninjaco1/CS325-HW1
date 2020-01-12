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
        insertionsort(temp)
        array.append(temp)

    print(array)
    #insertionsort(array)

def insertionsort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] <= array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

main()
