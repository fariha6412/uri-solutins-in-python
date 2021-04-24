n=int(input())
for i in range(n):
	lineli=list(map(str,input().split()))
	w1=input()
	newli=[]
	newlineli=""
	for w2 in lineli:
		if w2==w1:
			newli.append(str(len(newlineli)))
		newlineli+=w2+" "
	if len(newli)==0:
		print("-1")
	else:
		newline=' '.join(newli)
		print(newline)