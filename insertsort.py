from random import seed
from random import randint
import numpy as np
import time


def main():
    seed(1)
    #print(array)
    sort_data_file() # read data from files then sorts them


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


def sort_data_file():
    data = open("data.txt", "r")
    line = data.readlines()
    data.close()
    #print(line)
    array = []
    run_time = []
    for j in range(len(line)):
        temp = [int(i) for i in line[j].split() if i.isdigit()]
        print(temp)
        # run the sort three times then take the average of them
        temp_runtime = []
        sum = 0
        # calculate run time
        #for i in range(3):
            #start_time = time.time()#start time
        insertionsort(temp)
            #end_time = time.time() - start_time
            #temp_runtime.append(end_time)
            #sum += end_time
            #print(end_time)
        #temp_runtime.append(sum/3)
        #print(temp_runtime)
        # make the array a string
        #string = ""
        #for number in temp_runtime:
            #string += str(number) + " "
        #string += "\n"
        #run_time.append(string)
        #print(string)
        #end time
        array.append(temp)
    #print(run_time)
    #print(array)
    #insertionsort(array)
    out_file(array)
    #runtime_file(run_time)



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
