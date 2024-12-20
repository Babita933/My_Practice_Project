# 1)prime no
# num = 9
# fact_count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         fact_count = fact_count + 1
# else:
#     if fact_count == 2:
#         print('prime no')
#     else:
#         print('not a prime')
# factorial
# num=5
# fact=1
# for val in range(num,0,-1):
#     fact=fact*val
# print(fact)
# num = int(input("enter a number"))
# fact = 1
# if num == 0:
#     print("factorial is", 1)
# if num > 0:
#     for i in range(1, num+1):
#         fact = fact * i
# print("factorial of given number is", fact)
# add all the digit of a num
# num=1234
# dig_sum=0
# while num!=0:
#     rem=num%10
#     dig_sum=dig_sum+rem
#     num=num//10
# print(dig_sum)
# add all even no
# num = 2345
# even_sum = 0
# while num != 0:
#     rem = num % 10
#     if rem % 2 == 0:
#         even_sum = even_sum + rem
#     num=num//10
# print(even_sum)
# reverse a number
# num = 7654
# dig = len(str(num))
# pos = 10 ** (dig - 1)
# rev = 0
# while num != 0:
#     rem = num % 10
#     rev = rev + rem * pos
#     num = num // 10
#     pos = pos // 10
# print(rev)
# palidrome number
# num = 12321
# dup = num
# rev = 0
# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# if rev == dup:
#     print('palindrome')
# else:
#     print('not a palindrome')
# Composit Number
# num=12
# fact_count=0
# for den in range(1,num+1):
#     if num%den==0:
#         fact_count=fact_count+1
# if fact_count>2:
#     print('composit number')
# else:
#     print('not a composit number')
# # Armstrong Number
# num = 153
# dup = num
# power = len(str(num))
# res = 0
# while num != 0:
#     rem = num % 10
#     res = res + rem ** power
#     num = num // 10
# if dup == res:
#     print('Armstong number')
# else:
#     print('Not a Armstrong number')
# Disarum Number
# num = 135
# dup = num
# power = len(str(num))
# res = 0
# while num != 0:
#     rem = num % 10
#     res = res + rem ** power
#     power = power - 1
#     num = num // 10
# if dup == res:
#     print('Disarum Number')
# else:
#     print('Not a Disarum number')
# Convert int to binary
# num = 14
# pos = 1
# res = 0
# while num != 0:
#     rem = num % 2
#     res = res + rem * pos
#     num = num // 2
#     pos = pos * 10
# print(res)
# Evil Number
# num = 17
# count = 0
# while num != 0:
#     rem = num % 2
#     if rem == 1:
#         count = count + 1
#     num = num // 2
# if count % 2 == 0:
#     print('Evil no')
# else:
#     print('odeous no')
# LCM
# num1 = 6
# num2 = 12
# if num1 > num2:
#     lcm = num1
# else:
#     lcm = num2
# while True:
#     if lcm % num1 == 0 and lcm % num2 == 0:
#         print(lcm)
#         break
#     else:
#         lcm = lcm + 1
# GCD
# num1 = 3
# num2 = 10
# if num1 > num2:
#     gcd = num2
# else:
#     gcd = num1
# while True:
#     if num1 % gcd == 0 and num2 % gcd == 0:
#         print(gcd)
#         break
#     else:
#         gcd = gcd - 1
# Polyprime Number
# num = 11
# dup = num
# for den in range(2, num // 2 + 1):
#     if num % den == 0:
#         print('not a polyprime no')
#         break
# else:
#     rev = 0
#     while num != 0:
#         rem = num % 10
#         rev = rev * 10 + rem
#         num = num // 10
#     else:
#         if dup == rev:
#             print('polyprime no')
#         else:
#             print('not a polyprime no')
# EMRIP NUMBER
# num = 13
# dup = num
# rev = 0
# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 2
# if dup != rev:
#     for den in range(2, dup // 2 + 1):
#         if dup % den == 0:
#             break
#     else:
#         for val in range(2, rev // 2 + 1):
#             if rev % val == 0:
#                 print(rev)
#                 break
#         else:
#             print('EMRIP number')
# else:
#     print('Not a EMRIP Number')
#Tech no
# num = 2025
# if len(str(num)) % 2 == 0:
#     fp = num // (10 ** (len(str(num)) // 2))
#     sp = num % (10 ** (len(str(num)) // 2))
# if (fp + sp) ** 2 == num:
#     print('Tech no')
# else:
#     print('not tech no')
#Happy no
# num = 13
# while num > 9:
#     res = 0
#     while num != 0:
#         rem = num % 10
#         res = res + rem ** 2
#         num = num // 10
#     num = res
# if num == 1 or num == 7:
#     print('happy')
# else:
#     print('not happy')
#EMRIP NUMBER
# num = 13
# dup = num
# rev = 0
# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# if dup != rev:
#     for val in range(2, dup // 2 + 1):
#         if dup % val == 0:
#             break
#         else:
#             for den in range(2, rev // 2 + 1):
#                 if rev % den == 0:
#                     print('not prime')
#                     break
#     else:
#         print(' emrip no')
# else:
#     print('not emrif no')
