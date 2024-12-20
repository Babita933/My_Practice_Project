# wap to find the table of the given number
# n = int(input("Enter number:"))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1
# WAP to enter two number and find avg
# a = float(input("Enter 1st number:"))
# b = float(input("Enter 2nd number:"))
# avg = (a+b)/2
# print(avg)
#print number from 1 to 100
# i =1
# while i<=100:
#     print(i)
#     i+=1
#print number from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1
l = [1,4,9,16,25,36,49,64,81,100]
x=49
i=0
while i < len(l) :
    if l[i] ==x:
     print("element found at index",i)
     break
    i+=1