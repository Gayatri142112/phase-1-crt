#write a python program to print sum of the elements in last column of a matrix
r,c=int(input("Rows: ")),int(input("coloumns: "))
l,sum=[],0
for i in range(r):
    l.append(list(map(int,input().split())))
for i in l:
        sum+=i[c-1]
print(sum)
