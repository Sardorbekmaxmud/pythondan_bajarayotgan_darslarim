# import math
#
# uzunlik = lambda pi, r: 2*pi*r
# print(uzunlik(math.pi,10))
#
# product = lambda x, y: x**y
# print(product(3, 2))

# def daraja(n):
#     return lambda x: x**n
#
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga,"
#       f"kubi {kub(3)} ga teng")

# Bu yerdan map() dan foydalanib misollar bor

# from math import sqrt

# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)
# def daraja2(x):
#     return x*x
#
# print(list(map(daraja2,sonlar)))
#
# kvadratlar = list(map(lambda x: x*x,sonlar))
# print(kvadratlar)
#
# kvadratlar2 = []
# for i in range(11):
#     kvadratlar2.append(i*i)
# print(kvadratlar2)

# a = [4,5,6]
# b = [7,8,9]
# a_plus_b  = list(map(lambda a,b:a+b,a,b))
# print(a_plus_b)
#
# ismlar = ['sardorbek','sanjarbek','asror','izzat','aziz','feruz']
# natija = list(map(lambda matn:matn.upper(),ismlar))
# print(natija)

# Bu yerdan filter() func ga doir misollar

import random as r

# sonlar = r.sample(range(100),10)
#
# def juftmi(x):
#     return x%2==0
#
# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)
#
# lam = list(filter(lambda son: son%2==0,sonlar))
# print(lam)

mevalar = ['olma','apelsin','nok','olcha','anor','kivi','banan','shaftoli','anjir']

# b_teng = list(filter(lambda meva: meva.startswith('b'),mevalar))
# print(b_teng)
#
# uzunlik_besh = list(filter(lambda besh: len(besh)<=5,mevalar))
# print(uzunlik_besh)

bosh_A_oxir_R = list(filter(lambda meva: meva.startswith('a') and meva.endswith('r'),mevalar))
print(bosh_A_oxir_R)





