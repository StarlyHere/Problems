n = int(input())
s = input()

anton_count = s.count("A")
danik_count = n - anton_count

if anton_count > danik_count:
    print("Anton")
elif anton_count == danik_count:
    print("Friendship")
else:
    print("Danik")
