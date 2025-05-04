# Prime number

# Read the number from the keyboard and check whether it is prime number or not

num1=int(input("enter the number:"))
if num1>0:
    ref=True
    for i in range(2,num1//2):
        if num1%i==0:
            ref=False
            break
    if ref:
        print(f"{num1} is a prime number")
    else:
        print(f"{num1} is not a prime number")
else:
    print(f"{num1} is not a prime number")


