# each pizza contains 4 slices here nm is no of members ps means no of pizza slices c is total no of slices  
''' nm,ps=map(int,input().split(" "))
c=nm*ps
if c%4==0:
    d=c//4
else :
    d=(c//4)+1
print(d)# here d is total no of pizzas '''
import math
n,x=map(int,input().split())
ns=n*x
np=math.ceil(ns/4)
print(np)
