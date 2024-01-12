n=int(input())
counter=0
for i in range(n):
    s=input()
    for j in s:
        if j=="+":
            counter+=0.5
        elif j=="-":
            counter-=0.5
        else:
            continue
print(int(counter))