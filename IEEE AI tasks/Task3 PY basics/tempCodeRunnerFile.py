def x(n1, n2, c):
    s = 0  
    for i in range(len(c)):
        if c[i].isdigit() and i != n1:
            s += 1
    if s != n1 + n2:
        print("No")
    else:
        print("Yes")

try:
    n1 = int(input())
    n2 = int(input())
    c = input()
    
    if n1 < 0 or n2 < 0:
        raise ValueError("No")
    
    x(n1, n2, c)
except ValueError as e:
    print("No", e)
except Exception as e:
    print("No", e)
