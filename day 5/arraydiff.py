#you are given an integer array and a positive integer k you have to tell if there exists a pair of integers in the given array such that ar[i]-ar[j]=ar[k]
l,d=map(int,input().split())
lst=list(map(int,input().split()))
for i in lst:
    for j in lst:
        if i-j==d:
            flag=1
x=True if flag==1 else False
print(x)
