# s= [[j for j in range(4)] for i in range(3)]
# двумерный список ген [[j for j in range(b)] for i in range(a)]
from random import randint
def double_list(row,colum):
    lst=[]
    for i in range(row):
        lst.append([])
        for j in range(colum):
            lst[i].append(randint(0,20))
        print()
    return lst
row,col = int(input('Write row: ')), int(input('Write colum: '))
duo_list= double_list(row,col)
def pr_doub(lst):
    for i in lst:
        print(*i,sep='\t', end ='\n')

pr_doub(duo_list)
# сумма всех эл двумерсписка
def sumd(lst):
    s=0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            s+=lst[i][j]
    return s
# su=sumd(duo_list)
# print(f'Result: {su}')
#
# сумма элементов кажлой строки
def sums(lst):
    s=0
    new=[]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            s += lst[i][j]

        # print(s, end=' ')
        new.append(s)
        s=0
    return new
# ne=sums(duo_list)
# print(ne)
#находит сумму эл по столбцам и записывает в список\
def sumr(lst):
    rowlst=[]
    for j in range(len(lst[0])):
        summ=0
        for i in range(len(lst)):
            summ += lst[i][j]
        rowlst.append(summ)
    return rowlst
# rws=sumr(duo_list)
# print(rws)

# меняет две сосед строки в двумерно по 1 разу

def task3(lst):
    for i in range(0,len(lst)-1, 2):
        lst[i],lst[i+1]=lst[i+1], lst[i]
    return lst

# res= task3(duo_list)
# print()
# pr_doub(res)

# фун меняет местами соседние столбцы по 1 разу

def task4(lst):
    for j in range(0,len(lst[0])-1,2):
        for i in range(len(lst)):
            lst[i][j], lst[i][j+1]=lst[i][j+1],lst[i][j]
    return lst
# res4=task4(duo_list)
# print()
# pr_doub(res4)

