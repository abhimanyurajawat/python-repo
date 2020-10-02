#Calc sum of digits of a given no.
print("enter any no.")
n=int(input())
ssum=0
while(n!=0):
    x=n%10
    n=n//10
    ssum+=x
print(ssum)
