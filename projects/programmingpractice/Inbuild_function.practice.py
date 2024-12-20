# check string is pallindrome or not
# var = 'malayalam'
# rev = ''
# for ind in range(-1, -(len(var) + 1), -1):
#     rev = rev + var[ind]
# print(rev)
# if var == rev:
#     print('pallindrome')
# else:
#     print('not')
# or
# s = 'malayalam'
# for ind in range(0, len(s) // 2):
#     if s[ind] != s[-ind - 1]:
#         print(' not pallindrome')
#         break
# else:
#     print('pallindrome')
# or
# s = 'racecar'
# ind = 0
# while ind != len(s) // 2:
#     if s[ind] != s[-ind - 1]:
#         print('not pallindrome')
#         break
#     ind += 1
# else:
#     print('Pallindrome')
# to print vowels in the string
# var = 'developer'
# res = ''
# for ch in var:
#     if ch in 'aeiou' or ch in 'AEIOU':
#         res = res + ch
# print(res)
# or using range
# s = 'developer'
# res = ''
# for ind in range(0, len(s) ):
#     if s[ind] in 'aeiouAEIOU':
#         res = res + s[ind]
# print(res)
# Wap to print only upper case character
# s='DeVeloper'
# res=''
# for ch in s:
#     if ch .isupper():
#         res+=ch
# print(res)
# or
# s='DeVeLoper'
# res=''
# for ch in s:
#     if 'A'<=ch<='Z':
#         res=res+ch
# print(res)
# or
# s = 'DeveLopErs'
# res = ''
# for ch in s:
#     if 'a' <= ch <= 'z':
#         res = res + ch
# print(res)
# Wap to printall the substring in given string
# s = 'happy'
# for sv in range(0, len(s)):
#     for ev in range(sv + 1, len(s) + 1):
#         print(s[sv:ev])
# or
# s='happy'
# for sv in range(0,len(s)):
#     for ev in range(sv+1,len(s)+1):
#         result=''
#         for ind in range(sv,ev):
#             result+=s[ind]
#         print(result)
###### WAP to print all sub pallindromein the string
# s = 'happy'
# for sv in range(0, len(s)):
#     for ev in range(sv + 1, len(s) + 1):
#         word = s[sv: ev]
#         if word == word[::-1]:
#             print(word)
# remove duplicate
# s = 'developers'
# p = ''
# for ch in s:
#     if ch not in p:
#         p += ch
# print(p)
#####WAP count occurance of every character of string
s = 'programming'
p = ''
for ch in s:
    if ch not in p:
        p += ch
for ch1 in p:
    print(f'{ch1}' == {s.count(ch1)})
