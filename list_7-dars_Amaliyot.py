#ism = ['Aziz','Izzat','Feruz','Sanjar']
#print("Salom", ism[0], "ishlaring yaxshimi?")
#print(ism[1], "va", ism[2], 'egizaklar')
#print(ism[-1], "g'ildirakni g'izillatib g'ildiratdi")

#sonlar = [32_334_788, 4,56,-68,2323,465,2]
#sonlar[0] = sonlar[4]
#sonlar[-1] = 4 +  sonlar[-3]
#del sonlar[-2]
#sonlar[2] = sonlar[3] * sonlar[1] - sonlar[2]
#print(sonlar)

#t_shaxslar = ["Imom Buxoriy", "Muhammad (s.a.v)"]
#z_shaxslar = ["Shavkat Mirziyoyev"]
#print("Men tarixiy shaxslardan", t_shaxslar.pop(1), "bilan,\nzamonaviy shaxslardan esa",z_shaxslar.pop(), "bilan\nsuhbat qilishni istar edim.")

friends = []
friends.append("Feruz")
friends.append("Aziz")
friends.append("Izzat")
friends.append("Asror")
friends.append("Shahboz")
print(f"Mehmonga chaqirgan do'stlarim {friends}")
friends.remove("Izzat")
friends.remove("Aziz")
print(f"Mehmonga kelaoladigan do'stlarim {friends}")
friends.insert(0, "Sanjar")
friends.insert(4, "Sardor")
friends.insert(3, "Eldar")
print(f"Mehmonga chaqirgan do'stlarim 2- ro'yxat {friends}")
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-3))
mehmonlar.append(friends.pop(-4))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-5))
print("\nKelgan mehmonlar:", mehmonlar)




