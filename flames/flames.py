def flames(string1,string2):
    string1=list(string1)
    string2=list(string2)
    
    #hint la itha podu....

    #Remove " " (all spaces) from the list
    for i in string1:
        if(i==" "):
            string1.remove(i)
    for i in string2:
        if(i==" "):
            string2.remove(i)


    i=0
    while(i<len(string1)):
        if string1[i] in string2:
            j=string2.index(string1[i])
            string1.pop(i)
            string2.pop(j)
            i-=1
        i+=1
    print(string1)
    print(string2)

    count=len(string1)+len(string2)
    print(count)



    flame=['l']  
    inde=0
    while(len(flame)>1):
        
        removed=(inde+count-1)%len(flame)
        print(flame.pop(removed))
        inde=(removed)%len(flame)


    dist={'f':"Friend",'l':"Love","a":"Affection",'m':"Marry",'e':"Enemy",'s':"Sister"}
    return dist[flame[0]]
name1="prasanth"
name2="saani"
value=flames(name1,name2)
print(value)