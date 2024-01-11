t = int(input())

for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))

    found = False
    for i in range(1, n-1):
        if ar[i] != ar[i-1] and ar[i] != ar[i+1]:
            print(i+1)
            found = True

    if not found:
        if ar[0] != ar[1]:
            print(1)
        else:
            print(n)
