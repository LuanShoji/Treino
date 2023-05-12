'''maior = list()
x = 600851475143
y = 1
a = 0
z = 0
while True:
    if x == 1:
        break
    elif y / y == 1 and y / 1 == y:
        z = x / y
        if y > a:
            a = y
            maior.append(y)
    x -= z
    y += 1
print(y)'''
maior = list()
y = 2
x = 600851475143
while x != 1:
    if x % y != 0:
        y += 1
    else:
        x = x / y
        maior.append(y)
        print(y)
print(f"\nO maior número é {max(maior)}")
