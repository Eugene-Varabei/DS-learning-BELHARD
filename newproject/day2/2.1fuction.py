# function factorial
# def fact (n)
#     if n ==0 or n ==1:
#         return 1
#     else:
#         return n * fact(n-1)

# вид функции
# def name(argum, *args, **kwargs):
#       действие
#       return result (or yield)


# Без возвр знач просто без ретерн
############# function
# даны два числа. необходимо анйти сред них наименьшее

import time
def minim(a,b):
    if a>b:
        return b
    elif a<b:
        return a
    else:
        return f'Числа {a} и {b} равны'
# res=minim(int(input('write number: ')),int(input('write number: ')))
# print(res)

# дано 2 нат числ, надо число а возвести в степент б

def poww(a,b):
    rs=1
    for i in range(b):
        rs *= a
    return rs

# res=poww(int(input('write number: ')), int(input('write number: ')))
# print(res)

#  два нат числ, а и б. Надо найти наибольшее общий делитель испольщуя алгоритм евклида

def mxdel(a,b):
    while b>0:
        a,b = b, a%b
    return a

# res= mxdel(int(input('write number: ')), int(input('write number: ')))
# print(res)

# нат числ необх найти или вывести все делители

def deli(a):
    print(1, end =' ')
    for i in range(2, a//2+1):
        if a%i==0:
            print(i, end =' ')
    print(a)

# deli(int(input('write number: ')))

# 2 нат числа, при этом а < б . надо найти все простые числа промежутке между а и б


def prom(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
def al_prs(a,b):
    for i in range(a,b+1):
        if prom(i):
            print(i, end =' ')
    print()



def ispros2(n):
    for i in range(2, int(n**0.5)+1):
        if n %i ==0:
            return False
    return True
def al_prs2(a,b):
    for i in range(a,b+1):
        if ispros2(i):
            print(i, end =' ')
    print()
# a=int(input('write number: '))
# b=int(input('write number: '))
# tstart1= time.time()
# al_prs(a,b)
# tstop1= time.time()
# tstart2= time.time()
# al_prs2(a,b)
# tstop2= time.time()
# t1=tstop1-tstart1
# t2=tstop2-tstart2
# print(t1,t2)


