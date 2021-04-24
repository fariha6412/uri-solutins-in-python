while True:
	n=int(input())
	if n==0:
		break
	li=list(map(int,input().split()))
	for i in li:
		if li.count(i)%2==1:
			print(i)
			break


