x = 0
y = 0
for c in range(0, 101, 1):
    y += c**2
    x += c
x = x**2
z = x - y
print(z)
print(x)
print(y)
