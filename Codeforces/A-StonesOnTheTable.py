n=int(input())
s=input()
counter=0
for i in range(n-1):
    if s[i+1]==s[i]:
        counter+=1
print(counter)