t=int(input())
numbers=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



for i in range (t):
    n=int(input())
    s=input()
    counter=0
    for char in s:
        temp=s.count(char)
        tempOne=numbers.index(char)
        if temp>=tempOne+1:
            counter+=1  
        s=s.replace(char,'')
    print(counter)
