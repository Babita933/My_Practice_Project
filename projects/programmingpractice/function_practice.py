# Prime Number
# def prime(n, fact_count=0):
#     for den in range(1, n + 1):
#         if n % den == 0:
#             fact_count += 1
#     return fact_count == 2
#
#
# num = 11
# print('Prime' if prime(num) else 'not a prime')
# Factorial Number
# def factorial(n,fact=1):
#     for val in range(1,n+1):
#         fact=fact*val
#     return fact
# num=5
# print(factorial(num))
# Add all digit
# def dig_sum(n,ans=0):
#     while n!=0:
#         rem=n%10
#         ans=ans+rem
#         n=n//10
#     return ans
# num=1234
# print(dig_sum(num))
# multiply all digit
# def dig_mul(n,res=1):
#     while n!=0:
#         rem=n%10
#         res=res*rem
#         n=n//10
#     return res
# num=1234
# print(dig_mul(num))
# Armstron number
# def Armstrong(n, power, res=0):
#     while n != 0:
#         rem = n % 10
#         res = res + rem ** power
#         n = n // 10
#     return res
#
#
# num = 153
# print('Armstrong' if Armstrong(num, len(str(num)) == num) else 'not Armstrong')
# Disarum number
# def Disarum(n, power, res=0):
#     while n != 0:
#         rem = n % 10
#         res = res + rem ** power
#         power -= 1
#         n = n // 10
#     return res
#
#
# num = 135
# print('Disarum ' if Disarum(num, len(str(num)) == num) else ' Not a Disarum no')
# add even digit
# def even_dig(n, evensum=0):
#     while n != 0:
#         rem = n % 10
#         if n % 2 == 0:
#             evensum = evensum + rem
#         n = n // 10
#     return evensum
#
#
# num = 1234
# print(even_dig(num))
# Add odd number
# def odd_num(n,oddsum=0):
#     while n!=0:
#         rem=n%10
#         oddsum=oddsum+rem
#         n=n//10
#     return oddsum
# num=1356
# print(odd_num(num))
# Reverse a number
# def Reverse(n, rev=0):
#     dig = len(str(num))
#     posi = 10 ** (dig - 1)
#     while n != 0:
#         rem = n % 10
#         rev = rev + rem * posi
#         n = n // 10
#         posi = posi // 10
#     return rev
#
#
# num = 1234
# print(Reverse(num))
# Pallindrome
# def Pallindrome(n,rev=0):
#     while n != 0:
#         rem = n % 10
#         rev = rev * 10 + rem
#         n = n // 10
#     return rev == num
#
#
# num = 1221
# print('Pallidrome' if Pallindrome(num) else 'Not pallidrome')
# or
# def chk_pallindrome(n):
#     S = str(n)
#     reverse = S[::-1]
#     if S == reverse:
#         print('pallindrome')
#     else:
#         print('not prime')
#
#
# chk_pallindrome(1221)
# Composit number
# def composit(n, fact_count=0):
#     for den in range(1, n + 1):
#         if n % den == 0:
#             fact_count += 1
#     return fact_count > 2
#
#
# num = 11
# print('composit' if composit(num) else 'not composit no')
# Integer to binary
# def int_bin(n, res=0):
#     pos = 1
#     while n != 0:
#         rem = n % 2
#         res = res + rem * pos
#         n = n // 2
#         pos = pos * 10
#     return res
#
#
# num = 14
# print(int_bin(num))
# Binary to Integer
# def bin_int(n, res=0):
#     power = 0
#     while n != 0:
#         rem = n % 10
#         res = res + rem * (2 ** power)
#         n = n // 10
#         power = power + 1
#     return res
#
#
# num = 1110
# print(bin_int(num))
# Happy number
# def happy_no(n):
#     while n > 9:
#         res = 0
#         while n != 0:
#             rem = n % 10
#             res = res + rem ** 2
#             n = n // 10
#         n = res
#     return n == 1 or n == 7
#
#
# num = 13
# print('happy no' if happy_no(num) else 'not happy')
# Tech_no
# def Tech_no(n):
#     str_num = str(n)
#     if len(str_num) % 2 == 0:
#         fp = int(str_num[0:len(str_num) // 2])
#         sp = int(str_num[len(str_num) // 2:])
#         res = (fp + sp) ** 2
#         return res == num
#
#
# num = 2025
# print('Tech_no' if Tech_no(num) else ' Not Tech_no')
# Evil no
# def Evil(n, count=0):
#     while n != 0:
#         rem = n % 2
#         if rem == 1:
#             count += 1
#         n = n // 10
#     if count % 2 == 0:
#         return 'evil no'
#     return 'not evil no'
#
#
# num = 17
# print(Evil(num))
# Pallyprime
# def Rev(val, rev=0):
#     while val != 0:
#         rem = val % 10
#         rev = rev * 10 + rem
#         val = val // 10
#     return rev
#
#
# def prime(n):
#     for den in range(2, n // 2 + 1):
#         if n % den == 0:
#             return 'false'
#         return ' true'
# 
#
# # def palyprime(num):
#     if prime(num) and Rev(num) == num:
#         return 'palyprime'
#     return 'not palyprime'
#
#
# num = 11
# print(palyprime(num))
# #strong number
# def Factorial(n, fact=1):
#     for val in range(1, n + 1):
#         fact = fact * val
#     return fact


# def strong(num, res=0):
#     while num != 0:
#         rem = num % 10
#         res = res + Factorial(rem)
#         num = num // 10
#     return res
#
#
# num = 145
# print('strong' if strong(num) == num else 'not strong')
#Emrip no
# def Reverse(n,rev=0):
#     while n!=0:
#         rem=n%10
#         rev=rev*10+rem
#         n=n//10
#     return rev
# def Prime(dig):
#     for den in range(2,dig//2+1):
#         if dig%den==0:
#             return False
#         return True
# num=21
# dup=Reverse(num)
# print('emrip' if dup!=num and Prime(num) and Prime(dup) else 'Not emrip')

