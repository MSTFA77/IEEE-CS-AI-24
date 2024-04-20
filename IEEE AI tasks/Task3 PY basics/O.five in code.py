def pa(n):
    return str(n) == str(n)[::-1]

def pr(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cdiv(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c
z=int(input())
nums = [] 
for i in range(z):
    nums.append(int(input()))
max_number = max(nums)
print("The maximum number:", max_number)

min_number = min(nums)
print("The minimum number:", min_number)

prime_count = sum(1 for num in nums if pr(num))
print("The number of prime numbers:", prime_count)

palindrome_count = sum(1 for num in nums if pa(num))
print("The number of palindrome numbers:", palindrome_count)

max_divisors_number = max(nums, key=cdiv)
print("The number that has the maximum number of divisors:", max_divisors_number)
