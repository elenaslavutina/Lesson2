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

for element in spisok:
    elem = element[1]
    print(elem)
    my_keys = elem.keys()
    print(my_keys)

    if elem.get('Название') not in list1:
        list1.append(elem.get('Название'))
    list2.append(elem.get('Цена'))
    list3.append(elem.get('Количество'))
    if elem.get('Единица измерения') not in list4:
        list4.append(elem.get('Единица измерения'))

print(list1)
print(list2)
print(list3)
print(list4)
dict2 = {"Название":list1,"цена":list2, "Количество":list3, "Единица измерения":list4}
print(dict2)

