num = int(input("enter any number "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []

for element in a:
	if element <= num:
		new.append(element)

print(new)