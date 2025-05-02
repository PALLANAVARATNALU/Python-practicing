# Armstrong Number

n=int(input("enter the number:"))
dummy_num=n
reverse_num=0
length_num=len(str(n))
while n>0:
    r=n%10
    reverse_num=reverse_num+(r**length_num)
    n=n//10
print(reverse_num)
if dummy_num==reverse_num:
    print(f"{reverse_num} is a armstrong number")
else:
    print(f"{reverse_num} is not a armstrong number")