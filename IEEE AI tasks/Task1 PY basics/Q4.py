def r(s):
    w = s.split()
    rw = w[::-1]
    s = ' '.join(rw)
    return s
x= input("Enter a sentence: ")
rs = r(x)
print("Reversed sentence:", rs)
