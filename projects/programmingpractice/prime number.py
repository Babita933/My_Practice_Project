num=7
fact_count=0
for den in range(1,num+1):
    if num%den==0:
        fact_count=fact_count+1
else:
    if fact_count==2:
        print('prime no')
    else:
        print('not a prime no')
