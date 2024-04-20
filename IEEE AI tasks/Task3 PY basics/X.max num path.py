def max_sum(a, n, m, i=0, j=0):
    if i == n-1 and j == m-1:
        return a[i][j]
    if i == n-1:
        return a[i][j] + max_sum(a, n, m, i, j+1)
    if j == m-1:
        return a[i][j] + max_sum(a, n, m, i+1, j)
    return a[i][j] + max(max_sum(a, n, m, i, j+1), max_sum(a, n, m, i+1, j))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(max_sum(a, n, m))
