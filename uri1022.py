n=int(input())
for i in range(n):
	li=list(map(str,input().split()))
	a=int(li[0])
	b=int(li[2])
	c=int(li[4])
	d=int(li[6])

	k=li[3]

	if k=='+':
		u=a*d+c*b
		l=b*d
	elif k=='-':
		u=a*d-c*b
		l=b*d
	elif k=='*':
		u=a*c
		l=b*d
	elif k=='/':
		u=a*d
		l=b*c
	q=float(u/l)
	if q>1:
		x=u
	else:
		x=l
	w=1
	for j in range(1,x+1):
		m=float(u/j)
		if int(m)==m:
			n=float(l/j)
			if int(n)==n:
				w=j
	s=str(u)+'/'+str(l)+' = '+str(int(u/w))+'/'+str(int(l/w))

	print(s)