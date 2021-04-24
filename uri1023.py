j=1
while True:
	n=int(input())
	if n==0:
		break
	if j!=1:
		print()
	li=[0 for i in range(0,301)]
	s=0
	d=0
	for i in range(n):
		a,b=map(int,input().split())
		s+=a
		d+=b
		li[int(b/a)]+=a
	print("Cidade#",'{}:'.format(j))
	k=0
	for i in range(301):
		if li[i]!=0:
			if k!=0:
				print(" ",end='')
			print('{}-{}'.format(li[i],i),end='')
			k+=1
	print()
	print("Consumo medio:",'{:.2f}'.format(float(d/s)),"m3.")
	j+=1