import random
z = 0
while True:
    a = random.randint(100, 999)
    b = random.randint(100, 999)
    x = a * b
    if str(x) == f"{x}"[::-1]:
        if x > z:
            z = x
        print(z)
