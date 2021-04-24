while True:
	matrix=[]
	n,m=map(int,input().split())
	if n==0 and m==0:
		break
	for i in range(n):
		a=[]
		line=input()
		for c in line:
			a.append(c)
		matrix.append(a)
	p,q=map(int,input().split())
	x=int(p/n)
	y=int(q/m)
	newmatrix=[]
	for i in range(n):
		b=[]
		for k in range(x):
			for j in range(m):
				for l in range(y):
					b.append(matrix[i][j])
			newmatrix.append(b)
	for i in range(p):
		for j in range(q):
			print(newmatrix[i][j],end='')
		print()