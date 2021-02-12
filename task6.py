info = ""
spisok = []
i=1
list1 = []
list2 = []
list3 = []
list4 = []



while True:
   info = input("Введите информацию о товарах через пробел : название цена количество единица измерения (напримиемр шт). Для окончания введите выход : ")
   if info == "выход":
       break
   else:
       list = info.split()
       spisok.append((i,{"Название": list[0],"Цена": int(list[1]),"Количество": int(list[2]),"Единица измерения": list[3]}))
       i+=1
print(spisok)
dict2 = {}
for element in spisok:
    elem = element[1]
    print(elem)
    for key in elem.keys():
       print(key)

       dict2.update(key,elem[key])
       print(dict2)

    #dict2.update(elem)
#print(dict2)
