t=int(input())
for i in range(t):
	n=int(input())
	li=list(map(str,input().split()))
	newli=(' '.join(sorted(li)))
	print(newli)