def kvalue(weights, values, n, W):
    if n == 0 or W == 0:
        return 0
    
    if weights[n-1] > W:
        return kvalue(weights, values, n-1, W)
    
    inc = values[n-1] + kvalue(weights, values, n-1, W - weights[n-1])
    exc = kvalue(weights, values, n-1, W)
    
    return max(inc, exc)

N, W = map(int, input().split())

weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

max_value = kvalue(weights, values, N, W)
print(max_value)
