list = [1,'Betty',1.3,'puppy',3,-3,True,None]
for i in range (len(list)):
    print("Элемент списка",list[i]," является ",type(list[i]))

for idx, value in enumerate(list):
    print(f"Элемент {idx} списка {value} является ",type(value))

