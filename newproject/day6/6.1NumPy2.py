# обьединение одномерных массивов
import numpy as np
import time
# x1=np.random.randint(0,10,5)
# x2=np.random.randint(0,10,3)
# x3= np.concatenate((x1,x2))
# print(x1)
# print(x2)
# print(x3)

# объединение двумерных массивов по вертикали доб нов строк
# x1=np.random.randint(0,10,(2,3))
# x2=np.random.randint(0,10,(4,3))
# x3= np.concatenate((x1,x2),axis=0)
# print(x1)
# print(x2)
# print(x3)
                # or
# x4=np.vstack((x1,x2))
# print(x4)

# объединение двумерных массивов по горизонтали доб нов столбц
# x1=np.random.randint(0,10,(3,3))
# x2=np.random.randint(0,10,(3,4))
# x3= np.concatenate((x1,x2),axis=1)
# print(x1)
# print(x2)
# print(x3)
#             # or
# x4=np.hstack((x1,x2))
# print(x4)

# арифмет операции производ по элементно
# x1=np.random.randint(0,10,5)
# x2=np.random.randint(0,10,5)

# 1. сложение оператор + или np.add(x1,x2)
# t_sta1=time.time()
# x3=np.add(x1,x2)
# t_sto1=time.time()
# t_sta2=time.time()
# x4=x1+x2
# t_sto2=time.time()
# # print(x3)
# print(t_sto1-t_sta1)
# print(t_sto2-t_sta2)

# 2 вычитание - или np.subtract(x1,x2)
# 3 умножение * или np.multyply
# 4 деление / np.divide(x1,x2)
# x3= x1/x2
# print(x3)

# 5 целочисл деление // np.floor_divide
# print(np.floor_divide(x1,x2))

# 6 остаток % np.mod(x1,x2)
# print(np.mod(x1,x2))

# 7 степень ** or np.power(x1,x2)
# print(np.power(x1,x2))

# функция агрегирования
# x1=np.random.randint(0,100,10)
# 1 сумма эл массива
# print(np.sum(x1))
# 2 произедение эл массива
# print(np.prod(x1))
# 3 средарифм
# print(np.mean(x1))
# 4 стандартное отклонение
# print(np.std(x1))
# 5 дисперсия
# print(np.var(x1))
# 6 min el
# print(np.min(x1))
# 7 max el
# print(np.max(x1))
# 8 позиция мин  элементов np.argmin
# print(np.argmin(x1))
# 8 позиция max  элементов np.argmax
# print(np.argmax(x1))

# выборка из массива
x1=np.random.randint(0,100,10)
# срезы
# x2=x1[1::2]
# print(x2)
# x2[0]=-1 # заменяет значение и меняет в исодном

# замена не подходящего элемента на другое значение
# x2= np.where(x1%2==0, x1, -1)
# print(x2)
# x3=np.where(x1%2==0, x2, -1))

# выборка подхоядщих элементов
# x2=x1[x1%2==0]
# x2= x1[(x1>16) & (x1<62)]
# print(x1)
# print(x2)

