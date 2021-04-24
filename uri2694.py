import re

n=int(input())

for i in range(n):
	line=input()

	c=re.sub(r'\D'," ",line.lower()).split()

	c=[int(x) for x in c]
	print(c[0]+c[1]+c[2])