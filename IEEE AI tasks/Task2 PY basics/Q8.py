import random
import string
def generate_password(l):
    characters = string.ascii_letters + string.digits  
    password = ''.join(random.choice(characters) for _ in range(l))
    return password
x=int(input("Enter you length of Password : "))
random_password = generate_password(x)
print("your Password is : ", random_password)
