while True:
	try:
		line=input()
		a=set()
		odd=0
		for c in line:
			a.add(c)
		for c in a:
			if line.count(c)%2!=0:
				odd+=1
		if odd==0:
			print('0')
		else:
			print(odd-1)
	except EOFError:
		break