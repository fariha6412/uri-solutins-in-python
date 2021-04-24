lineli=list(map(str,input().split()))
n=int(input())
li=list(map(str,input().split()))
for w1 in li:
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