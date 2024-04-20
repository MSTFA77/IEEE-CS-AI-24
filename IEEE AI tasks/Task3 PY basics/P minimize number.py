n = int(input())
a = list(map(int, input().split()))
s = 0
while True:
    g = False
    for i in range(n):
        if a[i] % 2 != 0:
            g = True
            break
    if not g:
        s += 1
        for i in range(n):
            a[i] //= 2
    else:
        break

print(s)
