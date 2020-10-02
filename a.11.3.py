#Script to print sum of cubes of first N natural no.s
print("enter the value of n")
n=int(input())
i=1
summ=0
while(i<=n):
    summ+=i**3
    i+=1
print(summ)
