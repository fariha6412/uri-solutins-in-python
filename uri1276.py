while True:
	try:
		line=input()
		flag=0
		ch1=''
		ch2=''
		sap=False
		for c in "abcdefghijklmnopqrstuvwxyz.":
			if flag==0:
				if line.count(c)>0:
					ch1=c
					ch2=c
					flag=1
			elif flag==1:
				if line.count(c)>0:
					ch2=c
				else:
					if sap==True:
						print(", ",end='')
					print("%c:%c"%(ch1,ch2),end='')
					flag=0
					sap=True
			#print(line.count(c),flag)
		print()
	except EOFError:
		break
