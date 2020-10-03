def nonRepeated(arr):
    nonRepeat=0
    for i in range(len(arr)):
        nonRepeat^=arr[i]
    return nonRepeat
print(nonRepeated([11,11,1,1,3,2,2,9,3]))