# 1-javob 
def kopaytma(*sonlar):
    kopayt = 1
    for i in sonlar:
        kopayt *= i
    return kopayt

print(kopaytma(1,2,3,4,5))

# 2-javob
def malumot(ism,familya,**talabalar):
    talabalar['ism'] = ism.title()
    talabalar['familya'] = familya.title()
    return talabalar

talabalar_1 = malumot("sardorbek","maxmudov",tug_yil=2002,fakultet="software engineering".title())
talabalar_2 = malumot("asror","toshtemirov",tug_yil=1999,fakultet="data science".title())
print(talabalar_1)
print(talabalar_2)
   