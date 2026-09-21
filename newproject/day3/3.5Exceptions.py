# Конструкция try-except
# try:
#     danger smth
# except nameexceptions as s:
#     обработка исколючa

# a= int(input('Write num: '))
# b= int(input('Write num: '))
# lst=[1,2,3]
# try:
#     c=a//b
#     lst[3]=c
#     print(a//b)
# except ZeroDivisionError as ex:
#     print(f'Ошибка: {ex}')
#     c=-1
#     print(c)
# except IndexError as ex:
#     print(f'Ошибка: {ex}')
#     c=-1
#     lst.append(c)
#     print(lst)

number = -1
while number<=0:
    try:
        number= int(input('Write nat num: '))
    except ValueError as ex:
        print('Need to nat!! num: ')

print(number)

