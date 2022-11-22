# This code finds the length of the largest increasing sequence in a List
# Elements in the List cannot have duplicate elements

# indices_finder function is used to find the indices of all elements in Data > Value
# Time Complexity o(N)
def indices_finder(Data,Value):
    indices = []
    for i in range(len(Data)):
        if Data[i] > Value:
            indices.append(i)
    return indices

# rec_LIS finds the length of the longest sequence the first element of the array makes.
# Time Complexity o(2^N)
def rec_LIS(Data):
    indices = indices_finder(Data,Data[0])
    if indices:
        return 1 + max([rec_LIS(Data[idx:]) for idx in indices])
    else:
        return 1

# The main function to find the longest sequence length
# Time Complexity o(N*2^N)
def longest_increasing_sequence(Data):
    Max_LIS_length = 0
    for idx in range(len(Data)):
        Max_LIS_length = max(Max_LIS_length,rec_LIS(Data[idx:]))
    print("The longest increasing sequence length : " + str(Max_LIS_length))
    return(None)

longest_increasing_sequence([0,8,4,12,2,10])
longest_increasing_sequence([100, 22, 9, 33, 21, 50, 41, 60, 80])
longest_increasing_sequence([10,0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
