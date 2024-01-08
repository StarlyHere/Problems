t=int(input())
for i in range(t):
    n,b=list(map(int,input().split()))
    a=list(map(int,input().split()))
    product=1
    ls=[]
    for i in range(n):
        product*=a[i]

    if 2023%product==0:
        print("Yes")
        ls.append(2023//product)
        for i in range(b-len(ls)):
            ls.append(1)
        for i in range(len(ls)):
            print(ls[i], end=" ")      
    else:
        print("No")
    


