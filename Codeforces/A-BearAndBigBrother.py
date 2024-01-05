a,b=list(map(int,input().split()))
counter=0
while a<=b:
        a=a*3
        b=b*2
        counter+=1
print(counter)