def indices_finder(Data,Value):
    indices = []
    for i in range(len(Data)):
        if Data[i] > Value:
            indices.append(i)
    return indices


def rec_LIS(Data):
    indices = indices_finder(Data,Data[0])
    if indices:
        return 1 + max([rec_LIS(Data[idx:]) for idx in indices])
    else:
        return 1


A = rec_LIS([0,8,4,12,2,10])
print(A)
print(rec_LIS([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(rec_LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
