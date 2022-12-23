from son_topish import son_top_I, son_top_C

javob = True
while javob:
    x = 10
    hisob = son_top_I(x)
    hisob_2 = son_top_C(x)

    if hisob > hisob_2:
        print(f"Men {hisob_2} ta taxmin bilan topdim va yutdim")
    elif hisob < hisob_2:
        print(f"Siz {hisob} ta taxmin bilan topdingiz va yutdingiz")
    else:
        print(f"Durrang, ikkalamiz ham {hisob} ta taxmin bilan topdik")

    javob = int(input("\nYana o'yin o'ynaymizmi? yes (1)/ no (0)\n>>> "))