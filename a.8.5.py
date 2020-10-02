#Script to take month value in numeric format and display no. of days init.
m=int(input())
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print("this month have 31 days")
elif(m==4 or m==6 or m==9 or m==11):
    print("this month have 30 days only")
else:
    print("this month have only 28 or 29 days")
