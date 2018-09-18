#Sets
a = [1,2,2,2,3,3,3,4,4,5,6,7,7,8,9,9,9,9]

a = set(a)
a = list(a)
print(a)


#Loops
a = [1,2,2,2,3,3,3,4,4,5,6,7,7,8,9,9,9,9]
b = []

for i in a:
	if i in b:
		pass
	else:
		b.append(i)
print(b)
