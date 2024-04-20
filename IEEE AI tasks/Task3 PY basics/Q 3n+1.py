def sequence_length(n, count=1):
    if n == 1:
        return count
    elif n % 2 == 0:
        return sequence_length(n // 2, count + 1)
    else:
        return sequence_length(3 * n + 1, count + 1)
n = int(input())
length = sequence_length(n)
print(length)
