n = int(input())
s = input()

anton = s.count("A")
danik = n - anton

if anton > danik:
    print("Anton")
elif anton == danik:
    print("Friendship")
else:
    print("Danik")
