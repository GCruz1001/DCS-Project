import random
import matplotlib.pyplot as plt
import numpy as np


#Binary search function
def binary_search(array, val):
    #n is the length of the array
    n = len(array)
    #index i and j
    i = 0
    j = n - 1
    #we must keep count of comparisons
    cnt = 0
    #this is the part of the code that actually searches throught the indexes
    while (i <= j):
        m = (i+j)/2
        compare = array[i] - val  
        cnt = cnt + 1  
        #as soon as our value is found, we want to exit the loop
        if compare == 0:
            break
        #if not found and below, then its on the left side of the binary
        elif compare < 0:
            j = m - 1
        else:
        #else on the right side of the binary
            i = m + 1
    return cnt
        
#create an array with our n values prewritten from prompt
test_size = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
#create an empty array so we can store the averages and plot later
average_array = []
#begin the loop to look for averages
for n in test_size:
    array = random_array(n)
    #we must sort the array 
    array = sorted(array)
    cmp_count = 0
    sample_count = 100
    #calculation to find averages
    for _ in range(sample_count):
        val = random.randint(1, n + 3)
        count = binary_search(array, val)
        cmp_count = cmp_count + count
    avg = cmp_count / sample_count
#editing the blank array we made earlier in code with new found values
    average_array.append(avg)

# plot the graph
plt.plot(test_size, average_array)
plt.title('Binary Searching')
plt.ylabel('Average')
plt.xlabel('n')
plt.show()

#superimposing log_2 graph
#x_log = log(i * base)
#y = []
#plt.plot(x_log, y)
#plt.xlabel('x')

###############################################################################
# 2). function to create an array of random numbers of size 'n'
def random_array(n):
    array = []
    #Going through the array in order to fill the blank array created above
    while(len(array) < n):
        num = random.randint(1, n + 1)
        if num not in array:
            #array[] = []
            array.append(num)
    return array

def linear_search(array, x):
    n = len(array)
    i = 0
    while(i < n and array[i] != x):
        i = i + 1
    return i + 1

print('Linear Searching')

#Repeating 2 - 4 for a test size of 10 n 10-100
test_size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# 7). Need an array of average values
avg_array = []
#Using for loop to test all the values and find the averages
for n in test_size:
    array = random_array(n)
    cnt_comp = 0
    #cnt_val = cnt_comp + n
    cnt_sample = 100
    #Performing the search using our function created above
    for _ in range(cnt_sample):
        var = random.randint(1, 2 + n + 1)
        count = linear_search(array, var)
        #
        cnt_comp = cnt_comp + count
    average = cnt_comp / cnt_sample
    avg_array.append(average)
#Graphing results
plt.plot(test_size, avg_array)
plt.title('Linear Searching')
plt.xlabel('n')
plt.ylabel('Average')
plt.show

#Superimposed f(n) = n
x_val = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y_val = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.plot(x_val, y_val)

############################################################################

