a = int(input())
a1 = 0
a1 += a
b = []
c = 0
z = 0
x = 0
while a1 > 0:
    z += 1
    a1 = a1 // 10
for i in range(0, z):
    b.append((a // (10 ** i)) % 10)
for i in range(z - 1, -1, -1):
    print(b[i], end='')
    if i != 0 and ((i) % 3 == 0):
        print(',', end='')
