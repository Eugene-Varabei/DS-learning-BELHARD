import matplotlib
matplotlib.use('TkAgg') # отдельное окно для графиков
import matplotlib.pyplot as plt
# библиотека для построения 3d графики
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd


# названия кривых
# x=np.linspace(0,10,1000)
# plt.plot(x,np.sin(x), label='sin(x)')
# plt.plot(x,np.cos(x), label='cos(x)')
# #команда для добавления легенды на график
# plt.legend()
#
# #подпись осей
# plt.xlabel('X')
# plt.ylabel('Y')
#
# #подпись графика (назва)
# plt.title('Graphics sin(x) and cos(x)')
#
# plt.axis('equal')
# plt.show()



# Диаграмма рассеивания (точечная)

# x=np.linspace(0,20,100)
# y=x**0.33
# plt.scatter(x,y)
# plt.show()
#
# #виды маркеров в диаграмме рассеивания
# rng=np.random.RandomState(0) # отправная точка что бы одинаковые последоавтельности были
# #создадим список символов кот преобразуются в маркеры
# markers=['o', #кружок
#          '.', # точка
#          ',', # квадрат жел
#          'x', # х
#          '+', # плюс
#          '^', # треуг вверх
#          '<', # треуг вправо
#          '>', # треуг влево
#          's', # зел квадрат
#          'd'] # ромб
# for mark in markers:
#     plt.scatter(rng.rand(5),rng.rand(5),marker=mark, label=f'marker= {mark}')
# plt.legend()
# # укажем диапазон для оси Х
# plt.xlim(-0.1,1.5)
# plt.ylim(-0.1,1.5)
# plt.show()


#  доп настройки точек при отображении
# rng=np.random.RandomState(0)
# x=np.random.randn(100)
# y=np.random.randn(100)
# colors=rng.rand(100)
# size=1000*rng.rand(100)
#
# plt.scatter(x,y,c=colors,s=size,alpha=0.3, cmap='cool') #alpha это прозрачность, cmap это цветовая константа
# #добавлениие цветовой шкалы
# plt.colorbar()
# plt.show()

# # посмтроение контурных графиков
# def f(x,y):
#     return np.sin(x)**5 + np.cos(13+y*x)*np.cos(x)
# x=np.linspace(0,5,50)
# y=np.linspace(0,5,50)
#
# X,Y= np.meshgrid(x,y) # создание сетки из точек(х к у будет каждое пересечение)
# Z=f(X,Y)
# plt.contour(X,Y,Z, colors='black')
# plt.show()


# построение Гистограмм(столбчатая)
rng=np.random.RandomState(0)
# data=rng.normal(size=1300) #нормальное распределение
# plt.hist(data)
# plt.show()

# x1=rng.normal(0,0.8,1000)
# x2=rng.normal(0,1,1000)
# x3=rng.normal(0,2,1000)
#
# # создадим словарь внешних настроек графиков
# kwargs={'histtype': 'stepfilled', 'alpha': 0.3, 'density' : True, 'bins':40}
# plt.hist(x1,**kwargs)
# plt.hist(x2,**kwargs)
# plt.hist(x3,**kwargs)

# plt.show()


# zline=np.linspace(0,15,1000)
# xline=np.sin(zline)
# yline=np.cos(zline)
#
# # построение 3д проекции
#
# ax=plt.axes(projection = '3d')
# ax.plot3D(xline,yline,zline, 'gold')
#
# # сгененр и прорисуем точки пространства
# zdata=15*np.random.random(100)
# xdata=np.sin(zdata)+0.1*np.random.randn(100) #randn неравномерное распределение
# ydata=np.cos(zdata)+0.1*np.random.randn(100)
# ax.scatter3D(xdata,ydata,zdata,c=zdata, cmap='rainbow')
# plt.show()


# построение контурного графика в пространстве
# def f(x,y):
#     return np.sin(np.sqrt(x * x + y*y ))
# x=np.linspace(-6,6,1000)
# y=np.linspace(-6,6,1000)
# X,Y=np.meshgrid(x,y)
# Z= f(X,Y)
# ax=plt.axes(projection='3d')
# ax.contour3D(X,Y,Z, 40, cmap='rainbow')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# plt.savefig('imag.jpeg')
# plt.show()



