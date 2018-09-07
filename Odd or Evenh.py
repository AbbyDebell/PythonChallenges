randomNumber = int(input("Please enter a number "))
print(randomNumber)

if randomNumber % 2 == 0 and randomNumber % 4 != 0:
	print("even")
elif randomNumber % 4 == 0:
	print("multiple of 4")
else:
	print("odd")