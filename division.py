num = int(input("please enter a number"))
check = int(input("please enter a number which divides by the first"))

if num % check == 0:
	print(str(check) + "is a multiple of " + str(num))
else:
	print("these numbers don't divide")