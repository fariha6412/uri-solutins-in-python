li=[[0,400,15],[400,800,12],[800,1200,10],[1200,2000,7]]
n=float(input())
flag=0
for i in range(4):
	if n>=li[i][0] and n<=li[i][1]:
		flag=1
		r=li[i][2]
		m=n*r/100
		break
if flag==0:
	r=4
	m=n*r/100
print("Novo salario:",'{:.2f}'.format(n+m))
print("Reajuste ganho:",'{:.2f}'.format(m))
print("Em percentual:",r,"%")