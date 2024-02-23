#comparision of two strings and find the indices where string differs here codeforces is compared with the input
s=input()
s1="codeforces"
count=0
for i in range(len(s1)):
    if s[i]!=s1[i]:
        count+=1
print(count)
