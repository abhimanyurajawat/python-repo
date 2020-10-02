#script to print greater no. among three numbers.
print("enter any three no.s")
x=int(input())
y=int(input())
z=int(input())
if(x>y):
    if(x>z):
        print(x)
    else:
        print(z)
else:
    if(y>z):
        print(y)
    else:
        print(z)
