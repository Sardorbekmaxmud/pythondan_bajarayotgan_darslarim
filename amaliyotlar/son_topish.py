import random as r
def son_top_I(x):
    comp_num = r.randint(1,x)
    foy_son = int(input("Keling o'ylagan sonni topish o'ynaymiz\n"
                        f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?\n>>> "))
    add = 0
    while True:
        add+=1
        if comp_num > foy_son:
            foy_son = int(input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling!\n>>> "))
            # print(foy_son)
        elif comp_num < foy_son:
            foy_son = int(input("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling!\n>>> "))
            # print(foy_son)
        elif comp_num == foy_son:
            print(f"TOPDINGIZ! {comp_num} sonini o'ylagan edim. {add} ta taxmin bilan yutdingiz. Tabriklayman!!")
            return add
def son_top_C(x):
    com_num_2 = r.randint(1,x)
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman!\n")
    string = input("Son o'ylagan bo'lsangiz, istalgan tugmani bosing! ")
    sum = 0
    togri, plus, minus = 't', '+', "-"
    if string or '\n':
        while True:
            sum+=1
            javob = input(f"Siz {com_num_2} sonini o'yladingiz: to'g'ri bo'lsa ({togri}) ni bosing, men o'ylagan son bundan kattaroq bo'lsa ({plus}), yoki kichikroq bo'lsa ({minus}) ni bosing!\n>>> ".lower())
            if javob == '+':
                com_num_2 = r.randint(com_num_2+1,10-1)
            elif javob == "-":
                com_num_2 = r.randint(1,com_num_2-1)
            elif javob == "t":
                print(f"Soningizni {sum} ta taxmin bilan topdim\n")
                break
    return sum

