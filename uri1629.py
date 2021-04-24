while True:
	n=int(input())
	if n==0:
		break
	for i in range(n):
		line=input()
		k=0
		zeros=0
		ones=0
		ans=0
		for j in range(len(line)-1,-1,-1):
			if k%2==0:
				zeros+=(ord(line[j])-ord('0'))
			else:
				ones+=(ord(line[j])-ord('0'))
			k+=1
		while ones!=0:
			ans+=ones%10
			ones=int(ones/10)
		while zeros!=0:
			ans+=zeros%10
			zeros=int(zeros/10)
		print(ans)
