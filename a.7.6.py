#Script to check no. is three digit or not.
print("enter any number")
n= int(input())
if (n//100!=0 and n//1000==0):
    print("three digit no.")
else:
    print("not a three digit no.")
