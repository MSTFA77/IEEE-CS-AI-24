def get_numbers():
    while True:
        try:
            n = input("Enter a list of numbers separated by spaces: ").strip().split()
            n = [float(num) for num in n]
            return n
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")
def find_min(n):
    if not n:
        return None
    min = n[0]
    for num in n:
        if num < min:
            min = num
    return min
def find_max(n):
    if not n:
        return None
    max = n[0]
    for num in n:
        if num > max:
            max = num
    return max
def find_mean(n):
    if not n:
        return None
    total = sum(n)
    mean = total / len(n)
    return mean
def find_mode(n):
    if not n:
        return None
    f = {}
    for num in n:
        f[num] = f.get(num, 0) + 1
    maxf = max(f.values())
    modes = [num for num, freq in f.items() if freq == maxf]
    return modes
def find_median(n):
    if not n:
        return None
    sortednum = sorted(n)
    n = len(sortednum)
    if n % 2 == 0:
        return (sortednum[n // 2 - 1] + sortednum[n // 2]) / 2
    else:
        return sortednum[n // 2]
def find_range(n):
    if not n:
        return None
    return find_max(n) - find_min(n)
def find_variance(n):
    if not n:
        return None
    mean = find_mean(n)
    squared_diff = [(num - mean) ** 2 for num in n]
    variance = sum(squared_diff) / len(n)
    return variance
def find_STD(n):
    if not n:
        return None
    return find_variance(n) ** 0.5
def find_quartiles(n):
    if not n:
        return None, None, None
    sorted_numbers = sorted(n)
    n = len(sorted_numbers)
    Q2 = find_median(sorted_numbers)
    Q1 = find_median(sorted_numbers[:n // 2]) if n % 2 == 0 else find_median(sorted_numbers[:n // 2 + 1])
    Q3 = find_median(sorted_numbers[n // 2:]) if n % 2 == 0 else find_median(sorted_numbers[n // 2 + 1:])
    return Q1, Q2, Q3
def find_IQR(n):
    Q1, _, Q3 = find_quartiles(n)
    if Q1 is None or Q3 is None:
        return None
    return Q3 - Q1
n=get_numbers()
print("Minimum:", find_min(n))
print("Maximum:", find_max(n))
print("Mean:", find_mean(n))
print("Mode:",find_mode(n))
print("Median:", find_median(n))
print("Range:", find_range(n))
print("Variance:",find_variance(n))
print("Standard Deviation:", find_STD(n))
print("Quartiles (Q1, Q2, Q3):", find_quartiles(n))
print("Interquartile Range (IQR):", find_IQR(n))