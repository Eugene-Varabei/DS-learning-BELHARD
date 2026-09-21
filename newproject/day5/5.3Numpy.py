import numpy as np

# способы создания массива
# 1 на основе списка питона
# arr=np.array([i for i in range(10)])
# arr=np.array([1,2,3,4.1])
# arr = np.array([1,2,'3',4])

# 2создание массива заполненного нулями
# arr=np.zeros((100,100),dtype=float)

# 3 cоздание массива заполненного адзинками
# arr=np.ones((10,10), dtype=str)

# 4 cоздание массива заполненного укаханными знач
# arr=np.full(10,4)
#
# 5 заполн массива линейной последовательностью
# arr=np.arange(0,10,2)

# 6 заполн массива разбиением отрезка на равные части
# arr=np.linspace(1,10,5)

# 7 заполн массива случайными числами из отрезка (0;1)
# arr=np.random.random(5)

# 8 заполн массива целыми случ числами
# arr=np.random.randint(1,10,2)

# 9 заполн массива случ числами с целым и лдробным частями
# arr1=np.random.randint(1,10,5)
# arr2=np.random.random(5)
# arr=arr1+arr2
# arr=np.random.randint(1,10,5)+np.random.random(5)
# print(arr)


# извлечение инфы о размерности массива
x1=np.random.randint(1,20,5)
x2=np.random.randint(1,20,(3,4))
x3=np.random.randint(1,20,(3,4,5))

# print(x1)
# print()
# print(x2)
# print()
# print(x3)
# ndim возвр размерность массив
# print(f'x1.ndim: {x1.ndim}\nx2.ndim: {x2.ndim}\nx3.ndim: {x3.ndim}')

# shape возвращает каждой размерности
# print(f'x1.shape: {x1.shape} \nx2.shape: {x2.shape} \nx3.shape: {x3.shape}')

# size возвр общее кол-во эл
print(f'x1.size: {x1.size} \nx2.size: {x2.size} \nx3.size: {x3.size}')





