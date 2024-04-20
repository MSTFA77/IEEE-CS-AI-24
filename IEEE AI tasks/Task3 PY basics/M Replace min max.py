n = int(input())
a = list(map(int, input().split()))
maxindex = a.index(max(a))
minindex = a.index(min(a))
a[maxindex], a[minindex] = a[minindex], a[maxindex]

for i in range(n):
    print(a[i],end=" ")
