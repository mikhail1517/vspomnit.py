a = int(input())
a1 = 0
a1 += a
b = []
c = 0
z = 0
while a1 > 0:
    z += 1
    a1 = a1 // 10
if z >= 5:
    z = 5
for i in range(0, z):
    b.append((a // (10 ** i)) % 10)
if a // 100000 != 0:
    c = (a // 100000) * 100000
for i in range(0, z):
    c += b[i] * (10 ** (z - i - 1))
print(c)




print(dir())
