# 1-javob
##def toliq_malumot(ism,familya,tug_yil,yosh,tug_joy,el_manzil='',tel_raqam=None):
##    """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi,email
##       manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya"""
##    t_malumot = {'ismi':ism,
##                 'familya':familya,
##                 "tug'_yil":tug_yil,
##                 "yosh":yosh,
##                 "tug'_joy":tug_joy,
##                 "el_manzil":el_manzil,
##                 "tel_raqam":tel_raqam}
##    return t_malumot
##t_mal = toliq_malumot('Sardorbek','Maxmudov',2002,20,'Karmana',el_manzil='sardorbekmaxmudov33@gmail.com',tel_raqam=998_88_014_15_79)
##print(t_mal)

# 2-javob
##print("Saytimizdagi mijozlar ro'yxatini shakllantiramiz")
##mijozlar = []
##while True:
##    print("\nQuyidagi ma'lumotlarni kiriting: ")
##    ism = input("Ismi: ").title()
##    familya = input("Familyasi: ").title()
##    tug_yil = int(input("Tug'ilgan yili: "))
##    yosh = int(input("Yoshi: "))
##    tug_joy = input("Tug'ilgan joyi: ").title()
##    el_manzil = input("Email manzili: ")
##    tel_raqam = int(input("Telefon raqami: "))
##
##    mijozlar.append(toliq_malumot(ism,familya,tug_yil,yosh,tug_joy,el_manzil,tel_raqam))
##
##    javob = input("Yana ma'lumot kiritasizmi? (yes/no) ")
##    if javob == 'no':
##        break
##for mijoz in mijozlar:
##    if el_manzil:
##        el_manzil=mijoz['el_manzil']
##    elif tel_raqam:
##        tel_raqam=mijoz['tel_raqam']
##    else:
##        print("No'malum")
##    print(f"{mijoz['ismi']} {mijoz['familya']},{mijoz['tel_raqam']}")
    
# 3-javob
##def son_taqqos_max(son,son2,son3):
##    """Uchta son qabul qilib, ulardan eng
##    kattasini qaytaruvchi funksiya"""
##    if son>son2 and son>son3:
##        return son
##    elif son2>son3:
##        return son2
##    else:
##        return son3
##son_max = son_taqqos_max(47,27,13)
##print(son_max)

# 4-javob
##def rad_dia_per_yuz(radius):
##    Pi = 3.14
##    """Foydalanuvchidan aylaning radiusini qabul qilib olib,
##    uning radiusini, diametrini, perimetri va yuzini lug'at
##    ko'rinishida qaytaruvchi funksiya"""
##    javob = f"Radiusi {radius},\n"\
##            f"Diametri {radius*2},\n"\
##            f"Perimetri {2*Pi*radius},\n"\
##            f"Yuzi {Pi*radius*radius}"
##    return javob
##
##r_d_p_y = rad_dia_per_yuz(6)
##print(r_d_p_y)

# 5-javob
##def tub_son_topish(min,max):
##    """Berilgan oraliqdagi tub sonlar
##       ro'yxatini qaytaruvchi funksiya"""
##    sonlar = []
##    for n in range(min,max+1):
##        tub = True
##        if n == 1:
##            tub = False
##        elif n == 2:
##            tub = True
##        else:
##            for x in range(2,n):
##                if n % x == 0:
##                    tub = False
##        if tub:
##            sonlar.append(n)
##            
##    return sonlar
##        
##tub = tub_son_topish(1,100)
##print(tub)

# 6-javob
##def fibonacci(n):
##    sonlar = []
##    for x in range(n):
##        if x == 0 or x == 1:
##            sonlar.append(1)
##        else:
##            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
##        print(x)
##    return sonlar
##
##
##   
##df = fibonacci(15)
##print(df)







































    
