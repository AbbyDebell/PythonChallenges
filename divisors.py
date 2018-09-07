num = int(input("please enter a number"))
divisors = []

for i in range(1, num+1):
  if num % i == 0:
    divisors.append(i)
  else:
    pass
	
print(divisors)


