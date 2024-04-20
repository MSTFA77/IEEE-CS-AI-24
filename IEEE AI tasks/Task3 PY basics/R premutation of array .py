n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

x = 0
for i in range(n):
    if a[i] == b[i]:
        x += 1

if x == n:
    print("yes")
else:
    print("no")
