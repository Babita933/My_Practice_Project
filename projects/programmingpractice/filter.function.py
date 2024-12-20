# Armstrong num
# def Armstrong(n,res=0):
#     dup=n
#     power=len(str(n))
#     while n!=0:
#         rem=n%10
#         res=res+rem**power
#         n=n//10
#     return res==dup
# print(list(filter(Armstrong,range(1,50))))
# Strong Number
# def Factorial(n, fact=1):
#     for val in range(1, n + 1):
#         fact = fact * val
#     return fact
#
#
# def Strong(num, res=0):
#     dup = num
#     while num != 0:
#         rem = num % 10
#         res = res + Factorial(rem)
#         num = num // 10
#     return res == dup
#
#
#
#
# print(list(filter(Strong, range(100, 200))))
###or
# def strong(n, res=0):
#     dup = n
#     while n != 0:
#         rem = n % 10
#         fact = 1
#         for val in range(1, rem + 1):
#             fact = fact * val
#         res = res + fact
#         n = n // 10
#     return dup == res
#
#
# print(list(filter(strong, range(100, 200))))
# Happy Number
# def square(n, res=0):
#     while n != 0:
#         rem = n % 10
#         res = res + rem ** 2
#         n = n // 10
#     return res
#
#
# def Happy(dig):
#     while dig > 9:
#         dig = square(dig)
#     return dig == 1 or dig == 7
#
#
# print(list(filter(Happy, range(1, 100))))
####or
# def happy(n):
#     while n > 9:
#         res = 0
#         while n != 0:
#             rem = n % 10
#             res += rem ** 2
#             n = n // 10
#         n =res
#     return n == 1 or n == 7
#
#
# print(list(filter(happy, range(1, 50))))
# Factorial of given no range
# def Factorial(n):
#     fact = 1
#     for val in range(1, n + 1):
#         fact = fact * val
#     return fact
#
#
# print(list(map(Factorial, range(3, 8))))
