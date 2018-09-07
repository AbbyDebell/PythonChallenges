name = input("Enter your name: ")

print("Your name is " + name)

# DOB = int(input("Enter the year you were born "))
# print(DOB)

DOB = str(input("Enter your date of birth dd/mm/yyyy/"))

if len(DOB) == 10:
	print("Your date of birth is " + DOB)
else:
	print("This is not the correct format, please retry")

year = DOB[6:11]
print(year)

thisYear = 2018
age = thisYear - int(year)
print("You are "+ str(age) + " years old")


#if 10 > 6:
	# print("Your date of birth is " + DOB)
# else:
	# print("This is not the correct format")
	
	
