a = [10, 30, 60, 20, 40]
min1 = min2 = float('inf')
for num in a:
    if num < min1:
        min1 = num
    elif num < min2 and num != min1:
        min2 = num
print(min2)

b = [10, 30, 60, 20, 90]
min_num = float('inf')
for num in b:
    if num < min_num:
        min_num = num
print(min_num)

c = [10, 30, 50, 70, 20]
max_num = float('-inf')
for num in c:
    if num > max_num:
        max_num = num
print(max_num)

d = [20, 40, 70, 10, 80]
max_num = second_max = float('-inf')
for num in d:
    if num > max_num:
        max_num = num
    elif num > second_max and num != max_num:
        second_max = num
print(second_max)

