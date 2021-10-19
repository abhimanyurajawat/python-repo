class Solution:
    def frequency(self, A, N):
        count={i:0 for i in A}
        temp=[]
        for i in A:
            count[i]=count[i]+1
        print(count)
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ob=Solution()
    ob.frequency(a,n)