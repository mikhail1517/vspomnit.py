# k = int(input())
# ch1 = 0
# ch2 = 0
# ch3 = 0
# ch4 = 0
# for i in range(0, k):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         ch1 += 1
#     elif x < 0 and y > 0:
#         ch2 += 1
#     elif x < 0 and y < 0:
#         ch3 += 1
#     elif x > 0 and y < 0:
#         ch4 += 1
#
# print("""Первая четверть: {}
# Вторая четверть: {}
# Третья четверть: {}
# Четвертая четверть: {}""".format(ch1, ch2, ch3, ch4))

# m = input().split()
# z = 0
# for i in range(0, len(m), 2):
#     if not ((((len(m)) % 2) == 1) and (i + 1) == len(m)):
#         m[i], m[i + 1] = m[i + 1], m[i]
# st = ' '.join(m)
# print(st)
#
# m = input().split()
# print(m[-1],' '.join(m[:-1]))

# m = input().split()
# n = set(m)
# print(len(n))

# k = int(input())
# m = []
# for i in range(0,k):
#     m.append(int(input()))
# itog = int(input())
# b = False
# for z1 in range(0,k):
#     if m[z1]!=0:
#         if itog%m[z1] == 0:
#             for z2 in range(0,k):
#                 if m[z2]!=0:
#                     if itog/m[z1]!=1 and (itog/m[z1])/m[z2] == 1 and z2!=z1:
#                         b = True
#                 else:
#                     continue
#     elif itog == 0:
#         b = True
#         continue
# if b:
#     print('ДА')
# else:
#     print('НЕТ')



