stroka = input("Введите слова разделяя их пробелами  ")
list = stroka.split()

for i, x in enumerate(list):

    print(f"{i+1}  {x[:10]}  ")
