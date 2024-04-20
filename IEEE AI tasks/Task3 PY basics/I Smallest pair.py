t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    min_ = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            r = a[i] + a[j] + (j - i)
            min_ = min(min_, r)
    
    print(min_)
