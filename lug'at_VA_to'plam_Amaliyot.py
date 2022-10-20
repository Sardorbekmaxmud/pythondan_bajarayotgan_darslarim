##otam = {'ismi':'Xolmo\'min','tugilgan_yili':1975,'shahri':'Nurota'}
##onam = {'ismi':'Yulduz','tugilgan_yili':1979,'shahri':'Nurota'}
##ukam = {'ismi':'Sanjar','tugilgan_yili':2005,'shahri':'Karmana'}
##singlim = {'ismi':'Shabnam','tugilgan_yili':2013,'shahri':'Qibray'}
##print(f"Otamning ismi {otam['ismi']}, \
##{otam['shahri']} shahrida, \
##{otam['tugilgan_yili']}-yilda tug'ilgan.")
##print(f"Onamning ismi {onam['ismi']}, \
##{onam['shahri']} shahrida, \
##{onam['tugilgan_yili']}-yilda tug'ilgan.")
##print(f"Ukamning ismi {ukam['ismi']}, \
##{ukam['shahri']} tumanida, \
##{ukam['tugilgan_yili']}-yilda tug'ilgan.")
##print(f"Singlimning ismi {singlim['ismi']}, \
##{singlim['shahri']} tumanida, \
##{singlim['tugilgan_yili']}-yilda tug'ilgan.")

##sevimli_taomlar = {'Sanjar':'lavash',
##                   'Asror':'manti',
##                   'Ayam':'sho\'rva',
##                   'Xolmomin':'honim',
##                   'Shabnam':'chuchvara',
##                   }
##print(f"Sanjarning sevimli taomi {sevimli_taomlar['Sanjar']},\nTog'amni sevimli taomi {sevimli_taomlar['Asror']},\nAyamning sevimli taomi {sevimli_taomlar['Ayam']},\nDadamning sevimli taomi {sevimli_taomlar['Xolmomin']},\nShabnamning sevimli taomi {sevimli_taomlar['Shabnam']}.")

##pyIzohliL = {'variables':'o\'zgaruvchi',
##             'integer':'butun son',
##             'float':'haqiqiy son',
##             'list':'ro\'yxat',
##             'if':'agar',
##             'elif':'akisholda,agar',
##             'else':'aksholda',
##             'string':'matn',
##             'type':'turi',
##             'key':'kalit'
##             }
##izoh = input("Bironta so'z kiriting: ").lower()
##if izoh in pyIzohliL:
##    print(izoh)
##if izoh not in pyIzohliL:
##    print("Bunday so'z mavjud emas")
    
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit))

##kalit = input("Kalit so'z kiriting:").lower()
##tarjima = python_izohli_lugati.get(kalit)
##if tarjima==None:
##    print("Bunday so'z mavjud emas")
##else:
##    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

























