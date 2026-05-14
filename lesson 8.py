# цикл - это повторение каких либо действий заданое количество раз
#a=0
#while a<100

# a=100
# while a>=1:
#     print(a)
#     a=a-1

# a=4
# b=1
# while b<=10:
#     print(f"четыре={a*b}")
#     b+=1
#ИТЕРАЦИЯ-единичный цикл

# a=input("Введите города Беларуси").split(",")
# for i in a:
#     print(i)
#     print(f"Город:{i},{len(i)}")

#a=range(10)-от 0 до 10
#a=range(2,10)-от 1-ого до 2-ого значения
# a=range(2,10)
# print(list(a))
#range(2,10,2)-2,4,6,8
# a=int(input("Введите 10"))
# b=0
# for i in range(a):
#     b+=i
# print(b)

# a=int(input("Введите число"))
# b=1
# for i in range(1,a):
#     b=b*i
# print(b)

# from random import randint
# num=randint(1,100)
# print(num)

# a=int(input("Введите число"))
# from random import randint
# b=randint(1,100)
# c=b-a
# print(c)

from random import randint
level=1
money=10
while money<=1000000:
    print(f"Уровень-{level},баланс-{money}")
    rand=randint(1,100)
    num=int(input("Введите число"))
    if num==rand:
        print(f"Баланс-{money}")
        if money==1000000:
            print("поздравляю, вы выиграли")
            break
        choice=input("Продолжить да/нет")
        if choice=="нет":
            print("пока")
            break
        else:
            print("продолжаем лудоприключения")
            level+=1
            money*=10
    else:
        print(f"выпало число-{rand},you lost")
        choice=input("Продолжить да/нет")
        if choice=="нет":
            print("Пока")
        else:
            print("Продолжаем лудоприключения")
            money=10
            level=1