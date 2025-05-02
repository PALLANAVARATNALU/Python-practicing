# Disarium number

n=int(input("enter the number:"))
length_num=len(str(n))
remaindr=0
temp=n
sum1=0
while temp>0:
    remaindr=temp%10
    sum1=sum1+int(remaindr**length_num)
    temp=temp//10
    length_num=length_num-1
print(sum1)
if sum1==n:
    print(f"{sum1} is a disarium number")
else:
    print(f"{sum1} is not a disarium number")