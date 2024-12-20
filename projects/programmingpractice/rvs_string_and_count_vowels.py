# reverse a string and count the vowel
string = "my name is abinash"
rvs_str = ""
vowels = "aeiouAEIOU"
v_count = 0
for i in range(len(string) - 1, -1, -1):
    rvs_str += string[i]
print(rvs_str)
for i in rvs_str:
    if i in vowels:
        print(i)
        v_count += 1
print(v_count)
