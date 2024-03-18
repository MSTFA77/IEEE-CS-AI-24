def perfect(n):
    divsum = 0
    for i in range(1, n):
        if n % i == 0:
            divsum += i
    if divsum == n:
        return True
    else:
        return False
x = int(input("Enter a positive integer: "))
if x > 0:
    if perfect(x):
        print(f"{x} is a perfect number.")
    else:
        print(f"{x} is not a perfect number.")
else:
    print("Please enter a positive integer.")
