# factorial and recursive function

# factorial
n=int(input("enter the num:"))
sum1=1
for i in range(1,n+1):
    sum1*=i
print(sum1)


# using recursive method
def m1(n1):
    if n1==1:
        return 1
    return n1*m1(n1-1)
a=m1(6)
print(a)


# Count no. of vowels present in the string and read the string from keyboard
stri = input("enter the string:")
count=0
for i in stri:
    if i in "aeiouAEIOU":
        count+=1
print(count)