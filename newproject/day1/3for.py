# общ вид цикла for счеч in object(контейнер):
# блок кода действие
# n=[[1 for j in range(3)] for i in range(3)]
# for i in range(3):
#     for j in range(3):
#         print(n[i][j], end =' ')
#     print()
# n= []
# for i in range(1,5):
#     n.append(i)
# # print(*n, sep='*')
# for i in range(10,0,-2):
#     print(i, end='*')
# натур число н необходимо найти сумму первых n натур числе
# suma=0
# n= int(input('write number: '))
# for i in range(1,n+1):
#     suma+=i
# print(f'result: {suma}')
# дано число Н, найти Н факториал
#
# n= int(input('write number: '))
# import math
# a=math.factorial(n)
# print(a)
#
# if n==0:
#     print(1)
# else:
#     b=1
#     for i in range(1,n+1):
#         b*=i
#     print(b)
# lfyj 2 натур числа, найти их проихвеежднеие при этом оператор * не использовать
# a,b= int(input('write number: ')), int(input('write number: '))
# if b>a:
#     a,b=b,a
# multu=0
# for i in range(b):
#     multu+=a
# print(multu)

# неободимо найти все делители числа Н
# n=int(input('write number: '))
# print(1, end=' ')
# for i in range(2,n//2+1):
#     if n%i==0:
#         print(i, end=' ')
# print(n)

# даны два натур чисдла,  необзодимо вывести таблоицу из 0 размера из а и б

# a,b= int(input('write number: ')), int(input('write number: '))
# for i in range(a):
#     for j in range(b):
#         print(101, end='')
#     print()

# два нат числа таблицу из  при этом будет происходить чередование строк(одна из нулей б вторая из 1)

# a,b= int(input('write number: ')), int(input('write number: '))
# for i in range(a):
#     for j in range(b):
#         if i%2==0: #               print(i%2,end ='')
#             print('10', end='')
#         elif i%2==1:
#             print('01', end='')
#     print()

#

