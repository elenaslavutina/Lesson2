list_inp = input("Введите содержимое списка. Разделитель пробел. ")
list = list_inp.split()
index = 0
for x in list:
    index = index +1
    print(x)

print(index)
ind = 0
while ind <index-1:
    tmp =list[ind]
    list[ind] = list[ind+1]
    list[ind+1] = tmp
    ind = ind + 2
print(list)