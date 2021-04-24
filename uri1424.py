while True:
	try:
		n,m=map(int,input().split())
		li=list(map(int,input().split()))
		for j in range(m):
			k,c=map(int,input().split())
			d=-1
			try:
				for i in range(k):
					d=li.index(c,d+1)
				print(d+1)
			except Exception as e:
				print("0")
	except EOFError:
		break