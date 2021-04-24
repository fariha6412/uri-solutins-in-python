n=int(input())
for i in range(n):
	one=input()
	two=input()

	name=""
	for j in range(0,len(one)-1,2):
		name+=one[j]
		name+=one[j+1]
		name+=two[j]
		if (j+1)!=len(two):
			name+=two[j+1]
	print(name)