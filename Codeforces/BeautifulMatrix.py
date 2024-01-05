counter=0
row=0
column=0
moves=0
for i in range(5):
    m=list(map(int,input().split()))
    counter+=1
    if 1 in m:
        row=counter
        column=m.index(1) + 1
        moves= (abs(3-row)+abs(3-column))
        
        print(moves)
    



        