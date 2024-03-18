def sumE(n):
    t = 0
    a=[]
    if x <= 0:
       return f"Please enter a positive integer."
    else:
     for i in range(1, n + 1):
             if i % 2 == 0:
                t+= i 
                a.append(i)
    return f"The sum of even numbers from 1 to {n} is {t},({'+'.join(map(str, a))})."
x = int(input("Enter a positive integer: "))
print(sumE(x))       


