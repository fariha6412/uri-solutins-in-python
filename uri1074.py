n=int(input())

for i in range(n):
	d=int(input())
	if d==0:
		print("NULL")
	elif d%2==0:
		if d>0:
			print("EVEN POSITIVE")
		else:
			print("EVEN NEGATIVE")
	else:
		if d>0:
			print("ODD POSITIVE")
		else:
			print("ODD NEGATIVE")