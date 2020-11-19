x=2
for i in range(x):
    x+=2
    for j in range(x,1,-2):

        f=1
        for k in range(j):
            f*=1+j+k
            print(i,k,sep="@")
else:
    print(f)