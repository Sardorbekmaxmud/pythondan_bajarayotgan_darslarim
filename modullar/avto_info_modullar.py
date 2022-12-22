def avto_info(kompaniya,model,rangi,korobka,yili,narxi=None):
    avto = {
        "kompaniya":kompaniya,
        "model":model,
        "rangi":rangi,
        "korobka":korobka,
        "yili":yili,
        "narxi":narxi
    }
    return avto

def avto_kirit():
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting: ")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Yili: ")
        narxi = input("Narxi: ")

        avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narxi))

        javob = input("Yana avto qo'shasizmi? (yes/no): ")

        if javob == "no":
            break
    return avtolar

def avto_info_print(avto_info):
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].title()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yili']}-yil, {avto_info['narxi']}$")
