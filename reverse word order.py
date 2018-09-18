word = input("please input string including multiple words: ")

split = word.split()
back = split[::-1]

result = " ".join(back)
print(result)
# backwards = split.reverse()

# print(backwards)