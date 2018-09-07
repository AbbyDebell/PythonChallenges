a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in range(1, len(b)+1):
	if i in a and i in b:
		print(i)
	else:
		pass

		
students = ["abby", "charlotte", "tamsin", "grace", "miguela"]

name = input("please enter name of enrolled student ")

if name in students:
	print("This student is enrolled")
else:
	print("This student is not enrolled")