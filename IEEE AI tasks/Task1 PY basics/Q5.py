def p(w):
    w = w.lower()
    if w == w[::-1]:
        return True
    else:
        return False
x = input("Enter a word: ")
if p(x):
    print(f"The word '{x}' is a palindrome.")
else:
    print(f"The word '{x}' is not a palindrome.")
