##py_lugat = {
##    'boolean':'mantiqiy qiymat',
##    'float':'haqiqiy son',
##    'for':'biror amalni qayta-qayta bajarish',
##    'integer':'butun son',
##    'if':'shartni tekshrish',
##    'string':'matn',
##    'upper':'berilgan so\'zni hammasini kattalashtirish',
##    'items':'kalit va qiymatga birdaniga murojaat qilish',
##    'list':'lug\'at',
##    'sorted':'kelgan so\'zlarni alifbo tartibida tartiblash'
##    }
##for k, q in sorted(py_lugat.items()):
##    print(f"{k.title()} - {q.capitalize()}")

##davlatlar = {
##    'aqsh':'washington d.c',
##    'o\'zbekiston':'toshkent',
##    'tojikiston':'dushanbe',
##    'yaponiya':'tokio',
##    'hindiston':'dehli',
##    'italiya':'rim',
##    'malayziya':'kuala-lumpur',
##    'rossiya':'moskva',
##    'singapur':'singapur',
##    'qozog\'iston':'astana',
##    'qirg\'ziston':'bishkek',
##    'saudiya arabistoni':'ar-riyot'
##    }
##print("Dunyo davlatlari:")
##for davlat in sorted(davlatlar.keys()):
##    print(davlat.upper())
##    
##print("\nDavlatlarning poytaxtlari:")
##for poytaxt in sorted(davlatlar.values()):
##    print(poytaxt.title())
##    
##foy_chi = input("\nQaysi davlatning poytaxtini bilishni istaysiz?: ").lower()
##poy_taxt = davlatlar.get(foy_chi)
##if foy_chi in davlatlar:
##    print(f"{foy_chi.upper()}ning poytaxti {poy_taxt.title()} shahri")
##else:
##    print("Bizda bunday ma'lumot yo'q")

##menu = {
##    'osh':'15000',
##    'manti':'15000',
##    'norin':'30000',
##    'chuchvara':'20000',
##    'somsa':'5000',
##    'non':'4000',
##    'dolma':'25000',
##    'kabob':'7000',
##    'lag\'mon':'12000',
##    'bishtekis':'15000',
##    }
##buyurtmalar = []
##print("3 ta taom buyurtma bering.")
##for taom in range(3):
##    buyurtmalar.append(input(f"{taom+1}-taom: ").lower())
##
##for mahsulot in buyurtmalar:
##    if mahsulot in menu:
##        print(f"{mahsulot.title()} {menu[mahsulot]} so'm")
##    else:
##        print(f"Bizda {mahsulot} yo'q")
























