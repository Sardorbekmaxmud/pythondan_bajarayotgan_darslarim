# 1-javob
##def str_title(names):
##    big_latter = []
##    while names:
##        big_latter.append(names.pop().title())
##    return big_latter
##
##ismlar = ['sardorbek','anvar','umar','aziz','izzat']
##big_names = str_title(ismlar)
##
##two_list = []
##while big_names:
##    two_list.append(big_names.pop())
##print(two_list)

# 2-javob
##def str_letter(strings):
##    new_names = []
##    for i in range(len(strings)):
##        strings[i] = strings[i].title()
##        new_names.append(strings[i])
##    return new_names
##
##ismlar = ['ali', 'vali', 'hasan', 'husan']
##yangi_ismlar = str_letter(ismlar[:])
##print(ismlar)
##print(yangi_ismlar)

# 3-javob
##def baholar(ismlar):
##    baholar = {}
##    for i in range(len(ismlar)):
##        ism = ismlar[i]
##        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
##        baholar[ism] = baho
##    return baholar
##talabalar = ['ali','vali','hasan','husan']
##baholar = baholar(talabalar[:])
##print(baholar)
##print(talabalar)

