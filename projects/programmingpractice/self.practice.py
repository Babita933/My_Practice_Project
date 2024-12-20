L = [10, 20, 40, 50, 70, 30, 60]
min = float("inf")
for i in L:
    if i < min:
        min = i
print(min)
# Maximum
L = [10, 20, 40, 50, 70, 30, 60]
max = float("-inf")
for i in L:
    if i > max:
        max = i
print(max)
# 2nd minimum
L = [10, 20, 40, 50, 70, 30, 60]
min1 = min2 = float("inf")
for i in L:
    if i < min1:
        min2 = min1
        min1 = i
    else:
        if i < min2 and i != min1:
            min2 = i
print(min2)
# 2nd maximum
L = [10, 20, 40, 50, 70, 30, 60]
max1 = max2 = float("-inf")
for i in L:
    if i > max1:
        max2 = max1
        max1 = i
    else:
        if i > max2 and i != max1:
            max2 = i
print(max2)
# Ascending order
L = [10, 20, 40, 50, 70, 30, 60]
n = len(L)
i = 0
for i in range(i, n):
    for j in range(i + 1, n):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]
print(L)
# Dscending order
L = [10, 20, 40, 50, 70, 30, 60]
n = len(L)
i = 0
for i in range(i, n):
    for j in range(i + 1, n):
        if L[i] < L[j]:
            L[i], L[j] = L[j], L[i]
print(L)
# charecter accurance a from  string
s = "aabbcddccaaeedd"
char_count = {}
for i in s:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
print(char_count)
# word accurance
s = "Learning python python is is is  very very easy easy"
word = s.split()
word_count = {}
for i in word:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print(word_count)
# Remove duplicate charecter from list
s = "pyytthhhonnnnn"
unic_char = set()
result = []
for i in s:
    if i not in unic_char:
        unic_char.add(i)
        result += i
print(' '.join(result))
# remove Duplicate word
s = "learning learning python python is is very very easy easy"
word = s.split()
unic_word = set()
result = []
for i in word:
    if i not in unic_word:
        unic_word.add(i)
        result += i
print(' '.join(result))
# Remove special charecter from a string
s = "abc$%#def"
result = " "
for i in s:
    if i.isalnum() or i.isspace():
        result += i
print(result)
# Remove space from a string
s = " p  y   t  h o   n"
result = " "
for i in s:
    if i != " ":
        result += i
print(result)
# Reverse a string
s = "python"
reverse_string = " "
for i in range(len(s) - 1, -1, -1):
    reverse_string += s[i]
print(reverse_string)
# Reverse a word
s = "learning python is very easy"
word = s.split()
reverse_word = " "
for i in range(len(word) - 1, -1, -1):
    reverse_word += word[i]
print(reverse_word)
# prime number.py
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower + 1, upper):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

#
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[1::2])
# def factorial(n):
    if n==0:
     result=1
    else:
        result= n*factorial(n-1)
    return result


print("Factorial of 4 is:",factorial(4))
print("Factorial of 5 is:", factorial(5))
print("Factorial of 6 is:", factorial(6))
print("Factorial of 7 is",factorial(7))
