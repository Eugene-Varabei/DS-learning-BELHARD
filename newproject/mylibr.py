# Списки [] list(), lst[0], lst[1:]
# metods .append(n)  доп знач
# .extend(lst2) доп список
# len(lst) длинна списка
# .split() разбивает строку
# ' '.join(lst) собирает строку из спсика
# lst.insert(0, 'andr') добавить значение по индексу
# lst.remove('andr') удаляет первое вхожд эл
# lst.pop(1) удалит по 1 индексу
# lst.count('andr') кол-во в листе
# lst.reverse() меняет полрядок
# lst.sort() сортироует список
# спис выраэениЯ [i*2 for i in range(n)]     ,     n= [int(input()) for i in range(n)]
# с условием [i for i in range(21) if i%2==0]
# сорптировка n=len(lst)
#               for i in range(n-1):
#                     for j in range(n-1-1):
#                         if lst[j]>lst[j+1]:
#                             lst[j],lst[j+1] = lst[j+1],lst[j]
# двумерный список ген [[j for j in range(b)] for i in range(a)]
# функция созд список и заполняет его данным с клавы
# на вход принмимает размер списка и возвр сохданный список

# Подключение библиотек:
# import namebiblio    1
# from namebiblio import name_func    2

from random import randint
def inlst(size):
    lst=[]
    for i in range(size):
        lst.append(int(input(f'Write {i}-num for list: ')))
    return lst
def prn(lst):
    lst.sort()
    for i in range(len(lst)):
        print(lst[i], end ='\t')
    print()

# n = int(input('Write size: '))
# res = inlst(n)
# prn(res)
# Создание рандомного листа по 3 знач(размер, старт, стоп)
def inlst2(size, a, b):
    lst=[]
    for i in range(size):
        lst.append(randint(a,b))
    return lst
# n,a,b = int(input('Write size: ')), int(input('Write start num: ')), int(input('Write stop  num: '))

# prn(mlst)

# находит сумму эл списка
def suma(mlst):
    s=0
    for i in mlst:
        s+=i
    return s
# n = int(input('Write size: '))
# mlst = inlst2(n,0,20)
# print(mlst)
# print('Itogo:',suma(mlst))

# фун нахождениЯ четного эл списка
def chet(mlst):
    cnt=0
    for i in mlst:
        if i %2 ==0:
            cnt+=1
    return cnt
# result=chet(mlst)
# print(result)

# функция находит макс знач
def mxel(mlst):
    mx=mlst[0]
    for i in mlst[1:]:
        if i >mx:
            mx=i
    return mx
# res = mxel(mlst)
# print(res)

#mxpos находити возвр максим эл и позицию
def mxpos(mlst):
    mx=mlst[0]
    posi=0
    for i in range(1, len(mlst)):
        if mlst[i]>mx:
            mx=mlst[i]
            posi=i
    return posi, mx
# po,maxi=mxpos(mlst)
# print(f'Position: {po}, Max: {maxi}')

# f1 меняте местами два соседних элемента по одному разу
def f1(mlst):
    for i in range(0,len(mlst)-1,2):
        mlst[i],mlst[i+1]= mlst[i+1],mlst[i]
    print(mlst)
# f1(mlst)

# rev перворачивает список
def rev(mlst):
    n=len(mlst)
    for i in range(0,n//2):
        mlst[i],mlst[len(mlst)-i-1]=mlst[len(mlst)-i-1], mlst[i]
    print(*mlst)
# rev(mlst)