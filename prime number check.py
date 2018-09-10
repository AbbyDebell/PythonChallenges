num = int(input("please input a prime number "))
factors = [1, num]

for i in range(1, num+1):
	if num % i == 0 and i != num and i != 1 :
		factors.append(i) 
if len(factors) > 2:
	print("This is not a prime number. These are its factors: " + str(factors))
else:
	print("This number is prime")
		# print("This is not a prime number, these are its factors" + str(i))
	# else:
		# print("this is a prime number")

# print(factors)
		