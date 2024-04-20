def v(arr, n, t=0, c=0):
    if n == 0:
        return t / c if c != 0 else 0
    else:
        return v(arr, n-1, t + arr[n-1], c + 1)
n = int(input())
a = list(map(int, input().split()))
average = v(a, n)
print("{:.6f}".format(average))
