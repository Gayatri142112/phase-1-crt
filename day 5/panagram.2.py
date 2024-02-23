#write a python program to check given strings are panagrams or not
'''s1,s2=map(str,input().split())
if len(s1)==len(s2):
    if sorted(list(s1))==sorted(list(s2)):
        print(sorted(list(s1)))
        print(sorted(list(s2)))
        print("true")
    else:
        print("false")
else:
    print("false")'''

d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len(l[0])==len(l[1]):
    if sorted(list(l[0]))==sorted(list(l[1])):
        print("true")
    else:
        print("false")
else:
    print("false")
    
    
