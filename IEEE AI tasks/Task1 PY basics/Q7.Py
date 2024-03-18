def p(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    factors = list(set(factors))
    return factors
x = int(input("Enter a positive integer: "))
if x > 0:
    factors = p(x)
    print("Prime Factors:", ', '.join(map(str, factors)))
else:
    print("Please enter a positive integer.")
