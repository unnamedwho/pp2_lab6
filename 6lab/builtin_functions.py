#ex - 1
'''
def multiplication(list):
    product = 1
    for element in list:
        product *= element

    return product


list = [1, 3 ,4 ,6]
    
result = multiplication(list)
print(result)
'''
'''
list = [1, 3 ,4, 6]
product = 1
for element in list:
    product *= element

print(product)
'''
#ex - 2
'''
word = input("Enter your word: ")
sum_uppercaseletter = 0
sum_lowercaseletter = 0
for char in word:
    if char.isupper():
        sum_uppercaseletter += 1
    elif char.islower():
        sum_lowercaseletter += 1

print(sum_uppercaseletter)
print(sum_lowercaseletter)
'''
 #ex - 3

word = input("Enter your word: ")
word_original = word
word = word[::-1]
if word_original == word:
    print(f"Your word {word_original} is palindrome")
else:
    print(f"{word_original} is not palindrome")

