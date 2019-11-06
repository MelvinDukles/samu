string=str(input())
array=[]
for i in string:
	if i not in array:
		array.append(i)
print(len(array))
