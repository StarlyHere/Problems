n,k=map(int,input().split())
a= list(map(int,input().split()))
counter=0 
for i in range(0,n): 
    if a[k-1]==0 and a[i] == a[k-1]: 
        counter+=0 
    elif a[k-1]<=a[i]: 
        counter+=1 
    
print(counter)
