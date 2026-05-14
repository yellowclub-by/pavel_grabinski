# name = input("Введите ваше имя:")
# print("Здраствуйте", name)
# a = int(input("Введите ваш рост"))
# b = int(input("Введите ваш возраст"))
# print(a>=150 and b>=10)
#
#
#
#
#
#
#
# # Есть аквапарк с горкой, на которую пускают, если:
# # - возраст больше 10 лет
# # - или рост больше 150 см
# # Нужно написать программу, которая:
# # - приветствует посетителя по имени
# # - запрашивает возраст и рост
# # - проверяет возраст и рост на допустимые значения
# # - выдает решение в виде допуска на горку в виде: True или False
#
#
#

# name = input("Введите ваше имя:")
# print(name[-1])

# []-индекс 1 симво
# [:]-срез, берет часть строки
# a = "yellowclub-python"
# b = "yellowclub-photoshop"
# print(a[11:17])
# print(b[11:20])
# name="грабинский павел сергеевич"
# print(name[0:11])
# print(name[11:17])



# name = input("Введите имя с маленькой буквы:")
# print(name.upper())
# print(name.upper()[0] + name.lower()[1:])
# num = input("Введите номер телефона:")
# print(num.isdigit())

# name = "Yellow"
# print(name[2:6])
# print(name[4:6])


#шаги
#[начало:онец:шаг]
#конец до какого индекса не вкл. его
#шаг-прыжок через символ

# name="Yellow"
# print(name[0:10:2])
# print(name[::2])
# print(name[1:9:2])
# print(name[::-1])
# print(name[1:9:2])
#отрицательный шаг идет влево

# a="banana"
# print(a[0:6:2])
# print(a[0:6:5])
# print(a[1:6:2])
# print(a[-1:-7:-1])
# print(a[1:6:4])

#upper()- большие буквы
#lower()- маленькие буквы

# a= input("ведите первое слово")
# b= input("Введите второе слово")
# print(a.lower()==b.lower())

#capitalize-заглавная буква
# st=input("введите текст")
# print(st.capitalize())

# a=input("Введите имя")
# b=input("Введите фамилию")
# print(a.capitalize())
# print(b.capitalize())

#isdigit-проверка на цифры или нет
# year="1991a"
# print(year.isdigit())
# year1="1991"
# print(year1.isdigit())

# phone=input("Введите номер телефона")
# print(phone.isdigit())

#strip-удаление указаных символов
# phone="iphone 15"
# symbols="0123456789 "
# print(phone.strip(symbols))
# print(phone.strip("0123456789 "))

# model=" *Samsung 9"
# symbols=" *9"
# print(model.strip(symbols))

# name=input("Введите имя и номер телефона")
# letters=" а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я"
# symbols=" +0123456789"
# print(name.strip(symbols))
# print(name.strip(letters))

# letters="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
# x=int(input("Введите 1-ое число:").strip(letters))
# y=int(input("Введите 2-ое число:").strip(letters))
# print(x+y)

# name=(input("Введите имя"))
# surname=(input("Введите фамилию"))
# height=int (input("Введите рост"))
# weight=float(input("Введите вес"))
# print(f"Ученик:{name}, {surname} \n Рост:{height} \n Вес:{weight}")
#
# print(f"Имя:, {name}")
# print(f"Имя:{name}, Привет{name}")
# print(f"Имя:{name},Привет",)

# name = (input("Введите имя"))
# height=(input("Введите рост"))
# weight=int(input("Ведите вес"))
# form=(input("Введите класс"))
# phone=(input("Введите номер телефона"))
# letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
# print(name.capitalize())
# print(height)
# print(form.strip(letters))
# print(phone[8:12])
# w=weight
# proshel=w>40 and w<60
# print(f"имя:{name},рост:{height}, вес:{weight}, form:{form.strip(letters)}, н.тел.:{phone[8:12]}, {proshel}")

