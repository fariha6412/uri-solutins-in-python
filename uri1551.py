n=int(input())
for i in range(1,n+1):
	line=input()
	ct=0
	for c in "abcdefghijklmnopqrstuvwxyz":
		k=line.count(c)
		if k>0:
			ct+=1
	if ct>=26:
		print("frase completa")
	elif ct>=13:
		print("frase quase completa")
	else:
		print("frase mal elaborada")