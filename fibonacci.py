amount = int(input("how many numbers should i generate "))
fibonacci = [0, 1, ]

for i in range(1, amount+1):
	fibonacci.append(fibonacci[i]+fibonacci[i-1])
	
print(fibonacci)
	
	