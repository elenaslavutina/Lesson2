my_list = [7, 5, 3, 3, 2]
rating = int(input("Введите новый рейтинг "))
count = 0
max = len(my_list)
if rating in my_list:
    my_list.insert(my_list.index(rating)+my_list.count(rating),rating)
else:
    for i in range(max):
        if rating > my_list[i]:
            my_list.insert(i, rating)
            count = 1
            break
    if count!= 1:
        my_list.append(rating)


print(my_list)