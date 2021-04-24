n=int(input())
for i in range(n):
	k=int(input())
	words=[]
	for j in range(k):
		words.append(input())
	flag=1
	for j in range(1,k):
		if words[j]!=words[0]:
			flag=0
			break
	if flag==1:
		print(words[0])
	else:
		print("ingles")

		