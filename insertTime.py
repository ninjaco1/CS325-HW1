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
            insertionsort(temp)
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

def insertionsort(array):
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


def runtime_file(runtime):
    file = open("inserttime.txt","w")
    file.truncate(0)
    for string in runtime:
        file.write(string)
    file.close()



main()
