import math
n=int(input())
for i in range(n):
	d=int(input())
	if d==0 or d==1:
		print("Not Prime")
		continue
	r=math.sqrt(d)
	flag=1
	for j in range(2,r+1):
		if d%j==0:
			flag=0
			break
			