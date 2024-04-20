def d(n):
    if n < 10:
        print(n, end=" ")
    else:
        d(n // 10)  
        print(n % 10, end=" ")  
t = int(input())
for _ in range(t):
    y = int(input())
    d(y)
    print()  
