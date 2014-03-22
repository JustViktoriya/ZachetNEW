#Начало программы
#Нахождение длины массива А
na=raw_input("Enter length A")
#Массив А изначально пуст
mas_A=[]
print "A:"
#Ввод массива А
for i in range(0,na):
    a=raw_input()
    mas_A.append(a)
#Нахождение длины массива В
nb=raw_input("Enter length B")
#Массив В изначально пуст
mas_B=[]
print "B:"
#Ввод массива В
for i in range(0,nb):
    b=raw_input()
    mas_B.append(b)
#Массив С изначально пуст
mas_C=[]
#До конца массива А
for i in mas_A:
    #Первоначальное количество повторений элемента i в массиве А
    s=0
    """
    До конца массива В
    Считаем количество повторений элемента i в массиве В
    """
    for j in mas_B:
        if i==j:
            s=s+1
    # Если элемент не повторяется
    if s<2:
        #Записываем элемент в массив С
        c=raw_input()
        mas_C.append(c)
#Нахождение длины массива С
nc=len(mas_C)
#Если массив С пуст
if nc==0:
    #Выводим уведомление
    print ("C is empty" + \n)
#Если массив С не пуст
else:
    #Выводим массив С
    print ("C " + \n)
    for i in mas_C:
        print ("%7d", i)
#Конец программы
    
