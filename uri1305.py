while True:
	try:
		n=input()
		m=input()
		n=float(n)
		m=float(m)
		k=int(n)
		l=n-k
		if l>=m:
			k+=1
		print(k)
	except EOFError:
		break