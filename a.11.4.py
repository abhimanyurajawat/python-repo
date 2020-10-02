#Script to print sum of first N odd natural no.s
print("enter the value of n")
n=int(input())
i=1
summ=0
while(i<=2*n-1):
    summ+=i
    i+=2
print(summ)
