l = input()
a=[]
x=[]
for i in l:
    number=i.isdigit()
    if number==True:
        x.append(i)
 
 
x.sort()
 
for i in x:
    a.append(i)
    a.append("+")
 
a.pop()
for c in a:
    print(c, end='')