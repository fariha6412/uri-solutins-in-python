def hasharray(a,k):
	i=0
	sum=0
	for c in a:
		sum+=(ord(c)-65+k+i)
		i+=1
	return sum

def main():
	t=int(input())
	for i in range(t):
		n=int(input())
		total=0
		for j in range(n):
			line=input()
			total+=hasharray(line,j)
		print(total)

if __name__ =="__main__":
	main()