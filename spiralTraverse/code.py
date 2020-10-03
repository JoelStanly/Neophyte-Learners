def spiralTraverse(array):
    # Write your code here.
	column=len(array)-1
	row=len(array[0])-1
	direction=1
	res=[]
	i=-1
	j=0
	for _ in range((len(array)*len(array[0]))+min(len(array),len(array[0]))):
		if(direction==1):
			if(i<row):
				i+=1
				res.append(array[j][i])
			elif(j<column):
				j+=1
				res.append(array[j][i])
			else:
				direction=-1
				column-=1
		elif(direction==-1):
			if(i>len(array[0])-row-1):
				i-=1
				res.append(array[j][i])
			elif(j>len(array)-column-1):
				j-=1
				res.append(array[j][i])
			else:
				direction=1
				row-=1
	return res