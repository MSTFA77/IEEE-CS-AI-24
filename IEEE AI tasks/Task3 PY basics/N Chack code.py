def x(n1,n2,c):
    s=0  
    for i in range(len(c)):
      if c[i].isdigit() and i != n1:
        s += 1
    if s != n1 + n2:
      print("No")
    else:
       print("Yes")

n1=int(input())
n2=int(input())
c = input()
x(n1,n2,c)

