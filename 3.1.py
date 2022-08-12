def func(n1, n2):
    return n1 % n2 == 0


n1, nn2 = int(input()), int(input())
if func(n1, nn2):
    print('делится')
else:
    print('не делится')
