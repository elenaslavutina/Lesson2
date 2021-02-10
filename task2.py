list_inp = input("Введите содержимое списка. Разделитель пробел. ")
list = list_inp.split()

length = len(list)

ind = 0
while ind < length - 1:

    list[ind], list[ind+1] = list[ind+1], list[ind]

    #tmp =list[ind]
    #list[ind] = list[ind+1]
    #list[ind+1] = tmp


    ind = ind + 2

print(list)