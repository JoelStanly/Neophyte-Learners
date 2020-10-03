def maxIndexDiff(arr,n):
        maxIndex=0
        minimum=arr[0]
        minIndex=0
        for i in range(0,n):
            if(arr[i]>minimum):
                maxIndex=i
            elif(arr[i]<minimum):
                minimum=arr[i]
        if(arr[maxIndex]<=15):
            for j in range(1,maxIndex+1):
                if(arr[j]<=arr[maxIndex]):
                    return maxIndex-j
        for j in range(maxIndex+1):
            if(arr[j]<=arr[maxIndex]):
                return maxIndex-j

print(maxIndexDiff([34,8,10,3,2,80,30,33,1],9))