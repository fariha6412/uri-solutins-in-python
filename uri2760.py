a = input()
b = input()
c = input()

#first line
print('{0}{1}{2}'.format(a, b, c))
#second line
print('{1}{2}{0}'.format(a, b, c))
#third line
print('{2}{0}{1}'.format(a, b, c))
#last line
print('{0}{1}{2}'.format(a[0:10], b[0:10], c[0:10]))