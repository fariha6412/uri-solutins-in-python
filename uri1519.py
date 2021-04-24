while True:
	try:
		line=str(input())
		words=line.split()
		for w in words:
		    print(w)
	except EOFError:
		break