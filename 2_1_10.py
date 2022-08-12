n = int(input())
k = int(input())
b = []
z = 0
for i in range(0, n):
    b.append(i + 1)
while len(b) > 1:
    for i in range(0, len(b)):
        if b[i] != 0:
            z += 1
        if z % k == 0:
            b[i] = 0
            z = 0
        if k == 1:
            break
    for i in range(0, b.count(0)):
        b.remove(0)
print(b[0])
