#Script to check the year is leap or not.
print("enter any year")
n=int(input())
if(n%100):
    if(n%4):
        print("not a leap year")
    else:
        print("leap year")
else:
    if(n%400):
        print("not a leap year")
    else:
        print("leap year")
   
        
