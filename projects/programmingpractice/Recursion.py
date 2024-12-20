# Factorial
# def Factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * Factorial(n - 1)
#
#
# num = 5
# print(Factorial(num))
# Add all digit
# def Add_dig(n):
#     if n == 0:
#         return 0
#     return n % 10 + Add_dig(n // 10)
#
#
# num = 1234
# print(Add_dig(num))
# Multiply all digit
# def Mul_dig(n):
#     if n == 0:
#         return 1
#     return n % 10 * Mul_dig(n // 10)
#
#
# num = 1234
# print(Mul_dig(num))
# Armstrong number
# def Armstrong(n, power):
#     if n == 0:
#         return 0
#     return (n % 10) ** power + Armstrong(n // 10, power)
#
#
# num = 153
# power = len(str(num))
# print('Armstrong' if Armstrong(num, power) == num else 'Not Armstorng')
# Strong Number
# def Factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * Factorial(n - 1)
#
#
# def Strong(val):
#     if val == 0:
#         return 0
#     return Factorial(val % 10) + Strong(val // 10)
# num = 145
# print('Strong' if Strong(num) == num else 'Not Strong')
#
# # Happy Number
# def sq(n):
#     if n == 0:
#         return 0
#     return (n % 10) ** 2 + sq(n // 10)
#
#
# def Happy(val):
#     if val < 10:
#         return val == 1 or val == 7
#     return Happy(sq(val))
#
#
# num = 13
# print('Happy ' if Happy(num) else 'Not happy')
# Reverse a no
# def Rev(n, pos):
#     if n == 0:
#         return 0
#     return (n % 10) * pos + Rev(n // 10, pos // 10)
#
#
# num = 134
# power = len(str(num))
# print(Rev(num, 10 ** (power - 1)))
# or second way
# def Rev(n, res=0):
#     if n == 0:
#         return res
#     return Rev(n // 10, res * 10 + n % 10)
#
#
# num = 2190
# print(Rev(num))


# Integer to Binary
# def Int_bin(n, res=0):
#     pos = 1
#     if n == 0:
#         return 0
#     return Int_bin(n // 2, res + pos * n % 2)
#
#
# num = 14
# print(Int_bin(num))
# Disarum Number
# def Disarum(n, power):
#     if n == 0:
#         return 0
#     return (n % 10) ** power + Disarum(n // 10, power - 1)
#
#
# num = 135
# power = len(str(num))
# print('Disarum' if Disarum(num, power) == num else 'Not disarum')
# Prime number
# def prime(n,val=2):
#     if val==(val//2+1):
#         if n%val==0:
#             return 'false'
#         return prime(n,val+1)
#     return 'true'
# num=5
# print('prime' if prime(num) else 'not prime')
# Add all digit
# def Add(n):
#     if n == 0:
#         return 0
#     return n % 10 + Add(n // 10)
#
#
# num = 1234
# print(Add(num))
# Add Even no
# def Even(n):
#     if n == 0:
#         return 0
#     rem = n % 10
#     if rem % 2 == 0:
#         return rem + Even(n // 10)
#     return Even(n // 10)
#
#
# num = 1234
# print(Even(num))
# Add odd no
# def Odd(n):
#     if n==0:
#         return 0
#     rem=n%10
#     if rem%2!=0:
#         return rem+Odd(n//10)
#     return Odd(n//10)
# num=32517
# print(Odd(num))
# Armstrong number
# def Armstrong(n, power):
#     if n == 0:
#         return 0
#     return (n % 10)**power + Armstrong(n // 10, power)
#
#
# num = 153
# power = len(str(num))
# print('Armstrong' if Armstrong(num, power) == num else 'Not Armstrong')
#palyprime
def Rev(n, rev=0):
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev


def Prime(num):
    for den in range(2, num // 2 + 1):
        if num % den == 0:
            return 'false'
    return ' True'


def Palyprime(val):
    if Prime(val) and Rev(val) == val:
        return 'palyprime'
    return 'not pallyprime'


num = 11
print(Palyprime(num))
