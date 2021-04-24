while True:
	try:
		n,k=map(int,input().split())
		li=list(map(int,input().split()))
		li=sorted(li,reverse=True)
		sum=0
		for i in range(n):
			if i<k:
				sum+=li[i]%1000000007
			else:
				break
		print(sum)
	except EOFError:
		break