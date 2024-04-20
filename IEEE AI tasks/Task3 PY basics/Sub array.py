def x(n, a):
    for i in range(n):
        c=a[i]
        for j in range(i, n):
            print(max(a[j], c), end=" ")
t = int(input())
while t>0:
   n=0
   a=0
   n = int(input())
   a = list(map(int, input().split()))
   x(n, a)

