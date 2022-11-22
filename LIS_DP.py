# This code finds the length of the largest increasing sequence in a List
# Elements in the List cannot have duplicate elements
# This code uses the basics of dynamic programming for optimized calculation

# indices_finder function is used to find the indices of all elements in Data > Value
# Time Complexity o(N)
def indices_finder(Data,index,Value):
    indices = []
    for i in range(index,len(Data)):
        if Data[i] > Value:
            indices.append(i)
    return indices

# rec_LIS finds the length of the longest sequence the first element of the array makes.
# Time Complexity o(N)
def rec_LIS(Data,index,LIS_size_list):
    indices = indices_finder(Data,index,Data[index])
    if LIS_size_list[index]:
        return LIS_size_list[index]
    elif indices:
        return 1 + max([rec_LIS(Data,idx,LIS_size_list) for idx in indices])
    else:
        return 1

# The main function to find the longest sequence length
# Time Complexity o(N^2)
def longest_increasing_sequence(Data):
    Max_LIS_length = 0
    IS_size = [None]*len(Data)
    for idx in range(len(Data)-1,-1,-1):
        IS_size[idx] = rec_LIS(Data,idx,IS_size)
    #print(IS_size)
    print("The longest increasing sequence length : " + str(max(IS_size)))
    return None

longest_increasing_sequence([0,8,4,12,2,10])
longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
longest_increasing_sequence([10,0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
