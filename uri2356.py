while True:
	try:
		line1=input()
		line2=input()
		if (line2 in line1)==True:
			print("Resistente")
		else:
			print("Nao Resistente")
	except EOFError:
		break