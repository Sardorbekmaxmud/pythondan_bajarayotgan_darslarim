# 1-javob
##def tugilgan_yil(ism, yosh):
##    """Foydalanuvchi ismi va yoshini so'rab,
##       uning tug'ilgan yilini hisoblaydigan funksiya"""
##    print(f"{ism.title()} siz {2022-yosh}-yilda tug'ilgansiz.")
##
##tugilgan_yil(ism='sardorbek',yosh=20)

# 2-javob
##def kvadrat_kub(son):
##    """Foydalanuvchidan son olib, uning kvadrati va
##       kubini chiqaruvchi dastur."""
##    print(f"{son} ning kvadrati {son**2},\n"
##          f"kubi {son**3} ga teng.")
##
##kvadrat_kub(5)

# 3-javob
##def juft_toq(son):
##    """Foydalanuvchidan son olib,son juft yoki
##       toqligini konsolga chiqaruvchi funksiya."""
##    if son % 2 == 0:
##        print(f"{son} soni juft son")
##    else:
##        print(f"{son} soni toq son")
##
##juft_toq(565)
##juft_toq(345232)

# 4-javob
##def taqqoslov(num,son):
##    """Foydalanuvchidan ikkita son olib, ulardan
##       kattasini konsolga chiqaruvchi funksiya"""
##    if num > son:
##        print(f"{num}>{son}")
##    elif num < son:
##        print(f"{num}<{son}")
##    else:
##        print(f"Sonlar teng")
##        
##taqqoslov(8998,8998)
##taqqoslov(8998,899)
##taqqoslov(899,8998)

# 5-javob
##def two_numbers_daraja(num1,num2):
##    """Foydalanuvchidan x va y sonlarini olib,
##       x**y ni kosolga chiqaruvchi funksiya"""
##    print(f"{num1} ning {num2}-darajasi {num1**num2} ga teng")
##
##two_numbers_daraja(num1 = 94, num2 = 4)

# 6-javob
##def two_numbers_daraja(num,num_two=2):
##    """Foydalanuvchidan x va y sonlarini olib,
##       x**y ni kosolga chiqaruvchi funksiya"""
##    print(f"{num} ning {num_two}-darajasi {num**num_two} ga teng")
##
##two_numbers_daraja(11)

# 7-javob
##def tekshirish(son):
##    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
##       sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
##    for i in range(2,11):
##        if son%i==0:
##            print(f"{son} {i} ga qoldiqsiz bo'linadi")
##
##tekshirish(20)

