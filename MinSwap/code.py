def minSwap(arr):
    count=0
    i=0
    while(i<len(arr)):
        if(arr[i]!=i+1):
            count+=1
            index=arr[i]-1
            arr[i],arr[index]=arr[index],arr[i]
        else:
            i+=1
    return count
print(minSwap([7,1,3,2,4,5,6]))