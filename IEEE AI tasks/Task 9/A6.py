def main():
    n, m = map(int, input().split())
    colored = {'C', 'M', 'Y'}
    
    is_colored = False
    for _ in range(n):
        row = input().split()
        for pixel in row:
            if pixel in colored:
                is_colored = True
                break
        if is_colored:
            break
    
    if is_colored:
        print("#Color")
    else:
        print("#Black&White")

if __name__ == "__main__":
    main()
