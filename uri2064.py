k,m,n=map(int,input().split())
fav=input()
name=input()
maxc=0
for c in fav:
	maxc+=name.count(c)
rename=name
for i in range(n):
	a,b=map(str,input().split())
	name=name.replace(a,'1')
	name=name.replace(b,'2')
	name=name.replace('1',b)
	name=name.replace('2',a)
	k=0
	for c in fav:
		k+=name.count(c)
	if maxc<k:
		rename=name
		maxc=k
print(maxc)
print(name)
