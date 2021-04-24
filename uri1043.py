li=list(map(float,input().split()))
newli=sorted(li)

if newli[0]+newli[1]<=newli[2]:
	print("Area =",'{:.1f}'.format((li[0]+li[1])*li[2]/2))
else:
	print("Perimetro =",'{:.1f}'.format(li[0]+li[1]+li[2]))