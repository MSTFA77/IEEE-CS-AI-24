def can_reach_N(current, target):
    if current == target:
        return True
    elif current > target:
        return False
    else:
        return can_reach_N(current * 10, target) or can_reach_N(current * 20, target)

T = int(input())

for _ in range(T):
    N = int(input())
    result = can_reach_N(1, N)
    if result:
        print("YES")
    else:
        print("NO")
