def fact(n):
    fac = 1
    if n < 0:
        print("NOOOO!! num is negative ")    
    else:
        for i in range(1, n + 1):
            fac *= i
        return fac
x = int(input("Enter your positive num to find its factorial: "))
print(fact(x))
