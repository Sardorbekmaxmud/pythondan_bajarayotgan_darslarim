##adabiyot = {
##    'ism':'alisher navoiy',
##    'shahar':'xirot',
##    't_yil':1441,
##    'umr':60,
##    'asarlar':['layli va majnun',
##               'farxod va shirin',
##               'sabbai-sayyor']
##    }

##ilm_fan = {
##    'ism':'al-xorazmiy',
##    'shahar':'xiva',
##    't_yil':783,
##    'umr':67,
##    'asarlar':['arifmetika',
##               'zij',
##               'Surat al-Arz']
##    }

##sanat = {
##    'ism':'erkin vohidov',
##    'shahar':'farg\'ona',
##    't_yil':1936,
##    'umr':80,
##    'asarlar':['tongnafasi',
##               'o\'zbegim',
##               'qo\'shiqlarim sizga']
##    }

##internet = {
##    'ism':'stiv jobs',
##    'shahar':'kaliforniya',
##    't_yil':'1955',
##    'umr':56,
##    'asarlar':['steve jobs']
##    }

##malumotlar = [adabiyot, ilm_fan, sanat, internet]
##for malumot in malumotlar:
##    print(f"{malumot['ism'].title()} {malumot['t_yil']}-yilda\
## {malumot['shahar'].capitalize()}da tavallud topgan.\
## {malumot['umr']} yil umr ko'rgan.")

##for malumot in malumotlar:
##    print(f"\n{malumot['ism'].title()} ning mashhur asarlari: ")
##    for asar in malumot['asarlar']:
##        print(f"{asar.title()}")

##davlatlar = {
##    "Uzbekistan":{'poytaxt':'Toshkent',
##                   'hududi':448_978,
##                   'aholisi':33_000_000,
##                   'pul':'so\'m'},
##    "Rossiya":{'poytaxt':'Moskva',
##               'hududi':17_098_246,
##               'aholisi':144_000_000,
##               'pul':'rubl'},
##    "Aqsh":{'poytaxt':'Vashington',
##            'hududi':9_631_418,
##            'aholisi':327_000_000,
##            'pul':"dollar"},
##    "Malayziya":{'poytaxt':'Kuala-Lumpur',
##                 'hududi':329_750,
##                 'aholisi':25_000_000,
##                 'pul':'rinngit'}
##    }
##foyda = input("Davlat nomini kiriting: ").title()

##for key,value in davlatlar.items():
##    poytaxt = value['poytaxt']
##    hududi = value['hududi']
##    aholisi = value['aholisi']
##    pul = value['pul']
##    print(f"\n{key}ning poytaxti {poytaxt}\n"
##          f"Hududi: {hududi} kv.km\nAholisi: {aholisi}\nPul birligi: {pul}")

##if foyda in davlatlar:
##    info = davlatlar[foyda]
##    print(f"\n{foyda}ning poytaxti {info['poytaxt']}\n"
##          f"Hududi: {info['hududi']} kv.km\n"
##          f"Aholisi: {info['aholisi']}\n"
##          f"Pul birligi: {info['pul']}")
##else:
##    print("Bizda bu davlat haqida ma'lumot yo'q")
        
##kinolar = {
##    'ali':['Terminator','Rambo','Titanic'],
##    'vali':['Tenet','Inception','Interstellar'],
##    'hasan':['Abdullajon','Bomba','Shaytanat'],
##    'husan':['Mahallada duv-duv gap','John wick','Usmon']
##    }
##for k,v in kinolar.items():
##    print(f"\n{k.title()}ning sevimli kinolari:")
##    for kino in v:
##        print(kino)



