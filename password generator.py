# password generator 
import string
import random

choice = input("do you want a new password? yes/no ")


if choice == "yes":
	strength = input("how strong do you want your password? weak/medium/strong ")
	if strength == "weak":
		print("Here is your password: ")
		weakPassword = "".join(random.choices(string.hexdigits, k=4))
		print(weakPassword)
	elif strength == "medium":
		print("Here is your password: ")
		mediumPassword = "".join(random.choices(string.hexdigits + string.punctuation, k=6))
		print(mediumPassword)
	elif strength == "strong":
		print("Here is your password: ")
		strongPassword = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=12))
		print(strongPassword)
	else:
		print("this input is not correct please choose weak, medium or strong")
elif choice == "no":
	print("okay no new password this time")
else:
	print("this is not the correct input please choose yes or no")