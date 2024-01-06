n=int(input())
p=list(map(int,input().split()))
orange_juice=0
for i in range(n): 
    orange_juice+=p[i]

print(orange_juice/n)
