# 1-javob
print("Foydalanuvchidan buyurtma qabul qiluvchi dastur tuzing.")
buyurtmalar = []
n = 1
while True:
    savol = f"{n} - buyurtmani kiriting: "
    mahsulot = input(savol).lower()
    buyurtmalar.append(mahsulot)
    javob = input("Yana buyurtmaga mahsulot qo'shasizmi? (ha/yo'q)")
    if javob == "ha":
        n += 1
        continue
    else:
        break

# 2-javob
print("e-bozor uchun mahsulotlar va \
ularning narhlari lug'atini shakllantiruvchi dastur.")
mahsulotlar_narh = {}
while True:
    savol = (f"Mahsulot kiriting: ")
    key = input(savol).lower()
    narh = input(f"{key.title()}ning narhini kiriting: ")
    mahsulotlar_narh[key] = int(narh)
    javob = input("Yana mahsulot qo'shsangiz ( ha ) aksincha bo'lsa ( yo'q ) yozing ")
    if javob == 'ha':
        continue
    else:
        break
    
# 3-javob
for buyurtma in buyurtmalar:
    if buyurtma in mahsulotlar_narh:
        print(f"\n{buyurtma.title()} narhi {mahsulotlar_narh[buyurtma]} so'm")
    else:
        print(f"\nBizda {buyurtma.title()} yo'q")
