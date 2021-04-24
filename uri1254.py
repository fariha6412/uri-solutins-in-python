import re
while True:
	try:
		tag=input()
		rep=input()
		line=input()
		flag=0
		newline=""
		for c in line:
			if c=='<':
				flag=1
			if c=='>':
				flag=0
			if flag==1:
				newline+=c
			if flag==0 and c=='>':
				#print(newline)
				pattern=re.compile(re.escape(tag),re.I)
				newline=re.sub(pattern,rep,newline,0)
				print(newline,end='')
				newline=""
			if flag==0:
				print(c,end='')
		print()
	except EOFError:
		break;