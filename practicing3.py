# Palindrome - Numbers & String

# String palindrome
s1=input("enter the string:")
s2=""
for i in s1:
    s2=i+s2
print(s2)
if s2==s1:
    print(f"{s2} is a plindrome")
else:
    print(f"{s2} is  not a palindrome")


# Number palindrome
num1=int(input("enter the number:"))
dummy=num1
reverse_num=0
while num1>0:
    r=num1%10
    reverse_num=reverse_num*10+r
    num1=num1//10
print(reverse_num)
if dummy==reverse_num:
    print(f"{reverse_num} is a palindrome")
else:
    print(f"{reverse_num}is not a palindrome")