t=int(input())
for i in range(t):
	x,y=map(int,input().split('x'))
	for j in range(5,11):
		print("%d x %d = %d"%(x,j,x*j),end='')
		if x!=y:
			print(" && %d x %d = %d"%(y,j,y*j),end='')
		print()
