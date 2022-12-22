# 1-javob
# kopaytma = lambda x: x*10
# print(kopaytma(3))

# 2-javob
# add = lambda  a, b: a+b
# print(add(5,12))

# 3-javob
# import random as r
#
# tasodifiy_onta = r.sample(range(1000),10)
# print(tasodifiy_onta)
#
# kvadrat = list(map(lambda son: son**2,tasodifiy_onta))
# print(kvadrat)
#
# toq = list(filter(lambda son_toq: son_toq%2,tasodifiy_onta))
# print(toq)

# def tubmi(x):
#     if x % 2 == 0 or x < 2:
#         return False  # Son juft yoki 2 dan kichik bo'lsa
#     if x == 2 or x == 3:
#         return True  # Son 2 yoki 3 bo'lsa
#     for i in range(3, x, 2):
#         if x % i == 0:
#             return False
#     return True
#
# # print(tubmi(12))
#
# tub_sonlar = list(filter(tubmi, range(1,100)))
# print(tub_sonlar)
