n=int(input())
while n>0:
	n-=1
	k=int(input())
	li=list(map(int,input().split()))
	ct=0
	for i in range(k-1):
		for j in range(i+1,k):
			if li[i]>li[j]:
				ct+=1
				li[j],li[i]=li[i],li[j]
	print("Optimal train swapping takes %d swaps."%ct)
		