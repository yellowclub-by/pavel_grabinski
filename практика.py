#N1
# a=int(input("Введите ваш рост"))
# b=int(input("Введите любой рост"))
# if a > b:
#     print("я выше")
# else:
#     print("я ниже")

#N2
# name=[-2,-1,0,1,2,3,4,5,6,7,8]
# a=name[0]
# b=name[1]
# c=name[2]
# d=name[3]
# e=name[4]
# f=name[5]
# g=name[6]
# h=name[7]
# j=name[8]
# k=name[9]
# l=name[10]
# x=a+b+c+d+e+f+g+h+j+k+l
# print(x)

#/-нацело
#%-c остатком

# a=int(input("введите число"))
# if a < 99:
#     if a//10==a%10:
#         print("полиндром")
#     else:
#         print(" не полиндром")
# else:
#     print("ошибка")

# a=input("введите чай, сосиски, сахар")
# b=a.split(",")
# b.pop(1)
# b.remove("сахар")
# b.append("чайник")
# print(b)
# b.remove("сахар")
# b.append("чайник")
# print(b)

a=input("Введите 4 слова").split(",")
b=a[0][0]
c=a[1][0]
d=a[2][0]
e=a[3][0]
f=b+c+d+e
print(f)