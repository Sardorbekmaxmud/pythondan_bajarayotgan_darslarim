#juft_son = int(input("Juft son kiriting!!! "))
#if juft_son % 2 == 0:
#    print("Raxmat")
#else:
#    print("Bu son juft emas")

#yosh = int(input("Yoshingizni kiriting: "))
#if (yosh < 4 or yosh > 60):
#    print("Sizga kirish bepul")
#elif yosh <= 18:
#    print("sizga kirish 10000 so'm")
#elif yosh > 18:
#    print("Sizga kirish 20000 so'm")

#son1 = int(input("1 - sonni kiriting: "))
#son2 = int(input("2 - sonni kiriting: "))
#if son1 == son2:
#    print("Teng")
#elif son1 > son2:
#    print("1 - son katta 2 - son kichkina")
#elif son1 < son2:
#    print("2 - son katta 1 - son kichkina")

##mahsulotlar = ["go'sht","kartoshka","tuxum","kitob","karam",
##               "limon","uzum","olma","pamidor","non"]
##savat = []
##
##for i in range(5):
##    savat.append(input(f"savatga {i + 1} - mahsulotni qo'shing: "))
##if savat:
##    for mahsulot in savat:
##        if mahsulot in mahsulotlar:
##            print(f"Do'konimizda {mahsulot} bor")
##        else:
##            print(f"{mahsulot} do'konimizda yo'q")
##else:
##    print("Savatchangiz bo'sh")

##foydalanuvchilar = ["Anvar","Sardorbek","Elbek","Komil","G'ulom"]
##yangi_log = input("yangi login kiriting>>> ")
##
##if yangi_log:
##    if yangi_log.title() in foydalanuvchilar:
##        print(f"{yangi_log.title()} degan login band, yangi login tanlang!")
##    else:
##        print(f"Xush kelibsiz, {yangi_log.title()}!")
##else:
##    print("Siz loginni kiritmadingiz!")

##butun_son = int(input("Butun son kiriting: "))
##for i in range(2,11):
##    if butun_son % i == 0:
##        print(f"{butun_son} {i} ga qoldiqsiz bo'linadi")
##    else:
##        print(f"{butun_son} {i} ga qoldiqsiz bo'linmaydi")

#mahsulotlar = ["go'sht","kartoshka","tuxum","kitob","karam",
#              "limon","uzum","olma","pamidor","non"]
#savat = []
#bor_mahsulotlar = []
#mavjud_emas = []

#for i in range(5):
#    savat.append(input(f"Savatga {i + 1} - mahsulotni qo'shing: "))
#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            bor_mahsulotlar.append(mahsulot)
#        else:
#             mavjud_emas.append(mahsulot)
#    if not mavjud_emas:
#        print("Siz so'ragan barcha mahsulotlar bor")
#    else:
#        print(f"Quyidagi mahsulotlar do'konimizda yo'q,{mavjud_emas}")
#else:
#    ("Savatchangiz bo'sh")

pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, " ga teng.")

























