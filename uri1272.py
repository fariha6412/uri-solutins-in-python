n=int(input())
for i in range(n):
	line=input()
	word=""
	flag=0
	for c in line:
		if c.isalpha()==False:
			flag=0
			continue
		if flag==1 and c.isalpha()==True:
			continue
		if flag==0 and c.isalpha()==True:
			word+=c
			flag=1
	print(word)
		