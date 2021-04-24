while True:
	try:
		line=input()
		k=int(input())
		flag=0
		count=0
		for c in line:
			if c=='W':
				count+=1
				flag=0
			elif c=='R':
				flag+=1
				if flag==1:
					count+=1
				if flag==k:
					flag=0
		print(count)
	except EOFError:
		break