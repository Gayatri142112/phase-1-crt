#write a python program to print average of elements in given matrix
r,c=int(input("Rows: ")),int(input("coloumns: "))
l,sum=[],0
for i in range(r):
    l.append(list(map(int,input().split())))
for i in l:
       for j in i:
            sum+=j
print(sum)
print(sum/(r*c))
