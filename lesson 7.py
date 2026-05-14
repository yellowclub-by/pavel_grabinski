# if a<5:
#   a++
#if условие:
#   g-ua

#else:
#   print(">7")

# parol=input("Введите пароль")
# login=input("Введите логин")
# trueparol="1234"
# truelogin="p diddy"
# if parol==trueparol:
#     print("Пароль верный")
# else:
#     print("пароль не верный")
# if login==truelogin:
#     print("логин верный")
# else:
#     print("логин не верный")

#если а>10 и а=4
#если а<10
#if else print а у меня тоже есть птички

# a=int(input("Введите число"))
# if a<10:
#     if a==4:
#      print("venom")
# elif a>10:
#     print("муся это ты?")
# else:
#     print("опаааа у меня тоже есть птички")

# rating=int(input("Введите число от 0 до 10"))
# if 0<=rating<=10:
#     if rating==0:
#         print("фу")
#     elif rating==1:
#         print("не очень")
#     elif rating==2:
#         print("это вообще как у всех")
#     elif rating==3:
#         print("надо лучше")
#     elif rating==4:
#         print("все равно плохо")
#     elif rating==5:
#         print("уже лучше")
#     elif rating==6:
#         print("неплохо")
#     elif rating==7:
#         print("хорошо")
#     elif rating==8:
#         print("почти отлично")
#     elif rating==9:
#         print("отлично")
#     elif rating==10:
#         print("ну нифига ты молодец")
# else:
#     print("Введите число от 1 до 10")

# years=int(input("Введите ваш возраст"))
# a=100
# b=input("вы хотите кофе")
# if b=="да":
#     if years>18:
#         if a>150:
#             print("вот ваше кофе")
#         else:
#             print("попей водички)")
#
#     elif years<18 :
#         if a > 150:
#             print("на чай:)")
#         else:
#             print("попей водички)")
# elif b=="нет":
#     print("ну как хочешь")

# a=input("вы хотите домой?")
# if a=="да":
#     print("жаль тебя")
# else:
#     print("блин")

#если a>10 and a=20
#if a>10 and==20:код выполниться только если оба условия правильны
#   //код
#if a>10 ora==20:одно из условий верное
#   //код

#a=[1,2,3,4]
#b=2
#if b in a:
#   print("+")
#else:
#   print("-")
#if b not in a:
#   print("добавь")
#else:
#   print("есть в списке")

a=["хлеб","молоко","сахар","соль","пельмени"]
b=input("введите продукт")

if b not in a:
    a.append(b)
    print("добавили")
else:
    print("есть в списке")
