t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    a, b, cnt = float('inf'), float('inf'), 0
    for i in v:
        if a > b:
            a, b = b, a
        if i <= a:
            a = i
        elif i <= b:
            b = i
        else:
            a = i
            cnt += 1
    
    print(cnt)


        
   
        

            