import matplotlib
matplotlib.use('TkAgg') # отдельное окно для графиков
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
import pandas as pd


# подключение заготовленного стиля отображения графиков
# plt.style.use('classic') #Solarize_Light2


# rng=np.random.RandomState(0)
# x=np.linspace(0,50,500)
# y=np.cumsum(rng.randn(500,6), 0) #аккумулирующая сумма
# plt.plot(x,y)
# plt.legend('ABCDEF',ncol=2,loc='upper left')
# plt.show()


# гистрограммы и обводка гистограмм плавной кривой
# data=np.random.multivariate_normal([0,0],[[5,2],[2,2]], size=2000) # mean ценнтр промежутка, далее отклонения и дисперсия
# data=pd.DataFrame(data, columns=['x','y'])
# print(data)
# for col in 'xy':
#     plt.hist(data[col], alpha=0.5)
# plt.show()


# построим гладкую оценку распределения данных в гистограммах
# for col in 'xy':
#     sns.kdeplot(data[col], fill = True)
# plt.show()


# совместим  гистограмму и ядерную оценку распределения данных по гистограммам
# for col in 'xy':
#     sns.histplot(data[col],kde=True, stat="density") # это лучше чем distplot
# plt.show()


# построим график, кот отображает зависимость по знач среди четрыех параметрах

iris=sns.load_dataset('iris')
# print(iris) # ['species'].unique()
sns.pairplot(iris, hue='species', height = 2.5) # height instead of size
plt.show()


