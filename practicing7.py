# star pattern problems:

# pattern1:
for i  in range(1,6):
    print(i*"*")

# pattern2 : reverse to pattern1
for i in range(5,0,-1):
    print("*"* i)

# pattern3:
n=int(input("enter the num for series:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print(i*"*")

#pattern4 : reverse to pattern3
n=int(input("enter the num for series:"))
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print(i*"*")