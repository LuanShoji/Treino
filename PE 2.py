from time import sleep
a = 1
b = 1
x = 0
s = 0
while x <= 4000000:
    f = a + b
    a = b
    b = f
    if f % 2 == 0:
        s += f
    x = f
print(s)
#print(s)
