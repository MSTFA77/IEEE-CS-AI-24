def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    i = 0
    j = n - 1
    k = 0
    play1 = 0
    play2 = 0
    
    while i <= j:
        if a[i] >= a[j]:
            max_value = a[i]
            i += 1
        else:
            max_value = a[j]
            j -= 1
        
        if k % 2 == 0:
            play1 += max_value
        else:
            play2 += max_value
        k += 1
    
    print(play1, play2)

if __name__ == "__main__":
    main()
